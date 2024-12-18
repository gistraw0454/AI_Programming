import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


def createProblem(): ### TODO
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

def randomInit(p): ### TODO
    domain = p[1]   # domain: [varNams, low, up]
    low, up = domain[1], domain[2]
    init= []

    for i in range(len(low)):   # For each variable
        r= random.uniform(low[i],up[i]) # take a random value
        init.append(r)
    return init 
                   
def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain: [varNames, low, up]
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

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

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def mutants(current, p): ### TODO
    neighbors = []
    for i in range(len(current)):   # For each variable
        mutant = mutant(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA,p)
        neighbors.append(mutant)
    return neighbors    # neighbors 을 다 찾는다. 각각의 변수에대해 +-DELTA 해준다.

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple