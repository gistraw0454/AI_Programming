import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


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


def createProblem(): ### TODO
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    filename = input("Enter the file name of a function: ") # 파일 경로 입력 받기
    
    with open(filename, 'r') as file:   
        expression = file.readline().strip()    # 양쪽 공백 제거하여 파일 읽기

        varNames = []
        low = []
        up = []
        for line in file:
            (a, b, c) = line.strip().split(',')   # varNames, low, up을 list로 만들어 한줄읽을때마다 ',' 기준으로 split 해서 각각 넣기 
            varNames.append(a)
            low.append(float(b))
            up.append(float(c))
    
    domain = [varNames, low, up]    # domain를 list들의 list로 만들어 expression과 함께 return 
    return expression, domain


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


def randomInit(p): ### TODO
    (nop, domain) = p   # p가 (a,b) 형태를 가지므로 두값을 모두 받아와 domain만 사용
    varNames, low, up = domain  # domain값 (,,)로 따로 저장
    init = []   # 초기값 담는 list 생성
    for i in range(len(varNames)):
        initValue = random.uniform(low[i], up[i])    # low[i] ~ up[i]의 랜덤한 값을 뽑는다.
        init.append(initValue) # 초기값을 하나하나 담아주고 return 
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


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


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): ### TODO
    best = neighbors[0]
    bestValue = evaluate(best, p)
    
    for neighbor in neighbors[1:]:
        value = evaluate(neighbor, p)
        if value < bestValue:
            best = neighbor
            bestValue = value
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
