from numeric import *


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def mutants(current, p): ### TODO
    (nop, domain) = p  # p가 (a,b) 형태를 가지므로 두값을 모두 받아와 domain만 사용
    varNames, low, up = domain # domain값 (,,)로 따로 저장
    list1 = []  # 빈 리스트 생성 
    
    for i in range(len(current)):   # current만큼 돌면서 
        for d in [DELTA, -DELTA]:   # +,- 방향으로 변이를 다해본다.
            value = current[:]  # 완전히 복사한 리스트 생성
            value[i] = max(min(value[i] + d, up[i]), low[i])    # up, low를 벗어나지않게 이동시켜준다.
            list1.append(value) # 결과를 저장하고 list return 
    return list1

def bestOf(neighbors, p): ### TODO
    best = neighbors[0]
    bestValue = evaluate(best, p)
    
    for neighbor in neighbors[1:]:
        value = evaluate(neighbor, p)
        if value < bestValue:
            best = neighbor
            bestValue = value
    return best, bestValue

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
