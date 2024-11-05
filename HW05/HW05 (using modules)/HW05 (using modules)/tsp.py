import random
import math

NumEval = 0    # Total number of evaluations


def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    fileName = input("Enter the file name of a TSP: ")
    infile = open(fileName, 'r')
    # First line is number of cities
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()  # The rest of the lines are locations
    while line != '':
        locations.append(eval(line)) # Make a tuple and append
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table

def calcDistanceTable(numCities, locations): ### TODO
    table = []  # 빈 list 만들기
    for i in range(numCities):  # numcities만큼 돌면서 새로운 행 만들어 2d로 만들어주기
        table.append([0] * numCities)   # [0] 곱해주면됨
    
    for i in range(numCities):  # 모든 도시를 도는데
        for j in range(i + 1, numCities):   # 두도시의 거리를 비교함
            x = locations[i][0] - locations[j][0]  # x좌표 계산
            y = locations[i][1] - locations[j][1]  # y좌표 계산
            distance = math.sqrt(x**2 + y**2)   # x와 y사이의 거리구하기
            table[i][j] = distance  # 대칭으로 2d에 저장하기
            table[j][i] = distance
    
    return table # A symmetric matrix of pairwise distances

def randomInit(p):   # Return a random initial tour
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init


def evaluate(current, p): ### TODO
    ## Calculate the tour cost of 'current'
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids
    # Calculate the total tour cost for the current path
    global NumEval  # 전역변수 만들기
    NumEval += 1    # 수행할때마다 횟수를 1씩 증가시켜주기
    cost = 0

    for i in range(len(current)):
        if i == len(current) - 1:  # 마지막 도시면 처음으로 돌아가기
            next = 0
        else:
            next = i + 1  # 다음 도시로 이동
        cost += p[2][current[i]][current[next]] # 현재도시와 다음도시간의 거리비용 cost에 더하고 return
    return cost 

def inversion(current, i, j):  # Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

