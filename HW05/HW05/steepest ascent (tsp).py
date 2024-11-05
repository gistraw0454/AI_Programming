import random
import math


NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': (numCities, locations, table)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    
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


def steepestAscent(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

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



def mutants(current, p): # Apply inversion
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = inversion(current, i, j)
            count += 1
            neighbors.append(curCopy)
    return neighbors

def inversion(current, i, j):  ## Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def bestOf(neighbors, p): ### TODO
    best = neighbors[0] # 첫번째 neighbors를 받아온다.
    bestValue = evaluate(best, p)   # 첫번째 경로비용 계산
    
    for neighbor in neighbors[1:]:  # 나머지 경로를 돌면서 현재랑 비교하여 최솟값 찾기
        currentCost = evaluate(neighbor, p) # 현재와 이웃간 비용 계산
        if (currentCost < bestValue):  # best보다 더 낮으면 best(최소)값을 바꿔준다
            best = neighbor
            bestValue = currentCost
    return best, bestValue  # best와 bestValue 리턴

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

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

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

main()
