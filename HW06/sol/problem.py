import random
import math
DELTA = 0.01 

class Problem:
    def __init__(self):
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self): # interface�� ����
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
        # super().__init__(self) �Ѵ� ����
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

    def getDelta(self): # ��Ÿ ����
        return self._delta
    
    def getAlpha(self): # ���� ����
        return self._alpha

    def getDx(self):    # dx ����
        return self._dx

    def takeStep(self, x, v):   # ������ ���� �������� �̵�
        grad = self.gradient(x, v)  # ���� ��ġ������ ���� ���
        xCopy = x[:] # ����

        for i in range(len(xCopy)): # x���� ��ŭ �ݺ�
            xCopy[i] -= self._alpha * grad[i]   # ���� ���� �������� �̵� 
        
        if self.isLegal(xCopy):  # ������ Ÿ������ Ȯ�� �ϱ� 
            return xCopy
        else:
            return x

    def gradient(self,x,v): # �ش�κп����� ���⸦ ���Ѵ�.
        grad = []

        for i in range(len(x)):
            xCopyH = x[:]   # ����
            xCopyH[i] += self._dx # x_�� dx�� �����ش�. !
            g = (self.evaluate(xCopyH)-v)/self._dx  # ���� ���
            grad.append(g)  # ���� ����Ʈ�� �߰� 
        return grad # ����Ʈ ��ȯ

    def isLegal(self, x):   # low, up ����
        domain = self._domain
        low = domain[1]
        up = domain[2]
        flag = True

        for i in range(len(low)): # x���� ��ŭ ���鼭 �������� �ִ��� Ȯ��
            if x[i] < low[i] or x[i] > up[i]:
                flag = False    # ���� �����?
                break
        return flag

    def randomInit(self):
        domain = self._domain   # domain: [varNams, low, up]
        low, up = domain[1], domain[2]
        init= []
        for i in range(len(low)):   # For each variable
            r= random.uniform(low[i],up[i]) # take a random value
            init.append(r)
        return init


       
    def describe(self):
        print()
        print("Objective function:")
        print(self._expression)   # Expression
        print("Search space:")
        varNames = self._domain[0]
        low = self._domain[1]
        up = self._domain[2]
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
    
    def mutants(self, current):
        neighbors =[]
        for i in range(len(current)):
            mutant = self.mutate(current,i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current,i,-self._delta)
            neighbors.append(mutant)
        return neighbors
    
    def randomMutant(self,current): ### TODO  # ������ �Լ��� �ƴ�.
        i = random.randint(0,len(current)-1)
        if random.uniform(0,1)>0.5: # 0.5 Ȯ���� +,- ����
            d = self.getDelta()    
        else:
            d = -self.getDelta()
        return self.mutate(current, i, d)  # +,- �������� mutate ��Ŵ. (��ü �޼��� ȣ��)

class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []       # A list of tuples
        self._distanceTable = []

    ### Tsp methods
    # tsp�� createProblem�� setVariables �޼ҵ�� ����
    def setVariables(self):
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')  # ���� ��� �Է¹ޱ�
        self._numCities = int(infile.readline())
        locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            locations.append(eval(line))  # Ʃ�� ����� �߰��ϰ� �а� �ݱ�
            line = infile.readline()
        infile.close()
        self._locations = locations # ���� locations�� self._locations�� �ֱ�
        self._distanceTable = self.calcDistanceTable()  # table ��� self._distanceTable�� �α�


    def calcDistanceTable(self):
        table = [[0] * self._numCities for _ in range(self._numCities)]

        for i in range(self._numCities):
            for j in range(self._numCities):
                if i != j:
                    distance = math.sqrt((self._locations[j][0] - self._locations[i][0]) ** 2 + (self._locations[j][1] - self._locations[i][1]) ** 2)
                    table[i][j] = distance

        return table

    def randomInit(self):
        n =self._numCities # p[0]�� numcitiest
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        self._numEval += 1  # Problem���ִ� _numEval�� ++ ���ָ� �󸶳� ���� evalution �ϴ��� ��ô���ش�.

        n = self._numCities    # p[0] �� numcities
        table = self._distanceTable    # p[2] = distance table ��
        cost = 0    # 0�������� for ���� ���鼭 n-1��ŭ sum ����

        for i in range(n-1):
            locFrom = current[i]
            locTo = current[i+1]
            cost += table[locFrom][locTo]

        cost += table[current[-1]][current[0]]
        return cost
    
    def mutants(self, current):
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors

    def inversion(self, current, i, j): # �Ķ���͸� �ٲ��ش�.
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def randomMutant(self,current): # Apply inversion
        while True:
            i, j = sorted([random.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy


    # describeProblem
    def describe(self):
        print()
        n = self._numCities # p[0] �� self._numCities�ϱ� �����ϱ�
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations # p[1] �� self._locations�ϱ� �����ϱ�
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def tenPerRow(self):   # �״�� 
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()

    def report(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()
        print("Minimum tour cost: {0:,}".format(round(self._value)))   
        super().report()