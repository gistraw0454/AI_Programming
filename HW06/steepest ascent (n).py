from problem import Numeric


def main():
    
    p = Numeric()   
    p.setVariables()
    
    steepestAscent(p)
    
    p.describe()
    displaySetting(p)
    
    p.report()

def steepestAscent(p):
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current,valueC)


def bestOf(neighbors, p): ### TODO
    best = neighbors[0]
    bestValue = p.evaluate(best)
    
    for neighbor in neighbors[1:]:
        value = p.evaluate(neighbor)
        if value < bestValue:
            best = neighbor
            bestValue = value
    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()
