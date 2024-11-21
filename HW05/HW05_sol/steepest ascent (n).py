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
    fileName = input("Enter the file name of a function: ")
    infile = open(fileName, 'r')
    expression = infile.readline()
    varNames = []
    low = []
    up = []
    line = infile.readline()
    while line != '':
        data = line.split(',')  # read from CSV
        varNames.append(data[0])
        low.append(float(data[1]))
        up.append(float(data[2]))
        line = infile.readline()
    infile.close()
    domain = [varNames,low,up]
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


def randomInit(p):  ### TODO
    domain = p[1]   # domain: [varNams, low, up]
    low, up = domain[1], domain[2]
    init= []

    for i in range(len(low)):   # For each variable
        r= random.uniform(low[i],up[i]) # take a random value
        init.append(r)
    return init 


# 이거 어떻게 이루어졌는지 살펴보는거 나쁘지않음. !!!!!!!!!!!!!!!!!!!
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
    return eval(expr)   # eval로 한번에 계산 가능


def mutants(current, p): ### TODO
    neighbors = []
    for i in range(len(current)):   # For each variable
        mutant = mutant(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA,p)
        neighbors.append(mutant)
    return neighbors    # neighbors 을 다 찾는다. 각각의 변수에대해 +-DELTA 해준다.


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
    
    for i in range(1,len(neighbors)):
        newValue = evaluate(neighbors[i],p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
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
