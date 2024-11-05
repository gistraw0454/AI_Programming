from tsp import *


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

def bestOf(neighbors, p): ### TODO
    best = neighbors[0] # 첫번째 neighbors를 받아온다.
    bestValue = evaluate(best, p)   # 첫번째 경로비용 계산
    
    for neighbor in neighbors[1:]:  # 나머지 경로를 돌면서 현재랑 비교하여 최솟값 찾기
        currentCost = evaluate(neighbor, p) # 현재와 이웃간 비용 계산
        if (currentCost < bestValue):  # best보다 더 낮으면 best(최소)값을 바꿔준다
            best = neighbor
            bestValue = currentCost
    return best, bestValue  # best와 bestValue 리턴

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

main()
