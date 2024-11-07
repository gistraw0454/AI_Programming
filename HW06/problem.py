import random
import math


class Problem:
    def __init__(self):
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._expression = ''
        self._domain = []     # domain as a list
        self._delta = 0.01    # Step size for axis-parallel mutation

        self._alpha = 0.01    # Update rate for gradient descent
        self._dx = 10 ** (-4) # Increment for calculating derivative

    def setVariables(self):
        fileName = input("Enter the file name of a function: ")
        infile = open(fileName, 'r')
        self._expression = infile.readline()
        varNames = []
        low = []
        up = []
        line = infile.readline()
        while line != '':
            data = line.split(',')
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline()
        infile.close()
        self._domain = [varNames,low,up]

    def getDelta(self):
        return self._delta
    
    def getAlpha(self):
        return self._alpha

    def getDx(self):
        return self._dx

    def takeStep(self,x,v):
        pass

    def isLegal(self,x):
        pass

    def gradient(self,x,v):
        grad = []
        for i in range(len(x)):
            xCopyH = x[:]
            xCopyH[i] += self._dx
            g = (self.evaluate(xCopyH)-v)/self._dx 
            grad.append(g)
        return grad
       
    def describe(self):
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[1][0]
        low = self._domain[1][1]
        up = self._domain[1][2]
        for i in range(len(low)):
            print(" "+varNames[i]+":",(low[i],up[i]))
    
    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        Problem.report(self)

    def coordinate(self):
        c = [round(value,3) for value in self._solution]
        return tuple(c)
    
    def randomInit(self):
        domain = self._domain   # domain: [varNams, low, up]
        low, up = domain[1], domain[2]
        init= []
        for i in range(len(low)):   # For each variable
            r= random.uniform(low[i],up[i]) # take a random value
            init.append(r)
        return init

    def evaluate(self,current):
        self._numEval +=1
        expr = self._expression
        varNames = self._domain[0]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr) 
    
    def mutate(self, current,i,d):
        mutant = current[:]
        domain = self._domain        # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (mutant[i] + d) <= u:
            mutant[i] += d
        return mutant
    
    def mutants(self,current,p):
        neighbors = []
        for i in range(len(current)):   # For each variable
            mutant = self.mutate(current, i, self._delta, p)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta,p)
            neighbors.append(mutant)
        return neighbors


class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []       # A list of tuples
        self._distanceTable = []

    ### Tsp methods


