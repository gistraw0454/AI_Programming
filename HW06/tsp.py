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

def calcDistanceTable(numCities, locations): ### TODO 공통
    table = [[0] * numCities for _ in range(numCities)]
    for i in range(numCities):
        for j in range(numCities):
            if i!=j:
                distance = math.sqrt((locations[j][0] - locations[i][0]) ** 2 + (locations[j][1] - locations[i][1]) ** 2)
                table[i][j] = distance
    return table # A symmetric matrix of pairwise distances
    
def randomInit(p):   # Return a random initial tour
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init


def evaluate(current, p): ### TODO 공통
    # 얼마나 많이 evalution 하는지 추적하기 위해 
    global NumEval
    NumEval += 1

    n = p[0]    
    table = p[2]    # p[2] = distance table 임
    cost = 0    # 비용 초기화

    # 첫 도시부터, 맨 마지막 도시까지 투어하면서 distance table을 참고하여 비용 계산
    for i in range(n-1):
        locFrom = current[i]
        locTo = current[i+1]
        cost += table[locFrom][locTo]
    # 맨 마지막 도시에서 처음 도시로 돌아오는 비용을 고려해서 cost에 더해줌
    cost += table[current[-1]][current[0]] 
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

# def bestOf(neighbors, p): ### TODO steep만 적용
#     best = neighbors[0]
#     bestValue = evaluate(best, p)
    
#     for i in range(1, len(neighbors)):
#         newValue = evaluate(neighbors[i],p)
#         if newValue < bestValue:
#             best = neighbors[i]
#             bestValue = newValue
#     return best, bestValue