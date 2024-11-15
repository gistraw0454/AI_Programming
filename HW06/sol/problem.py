import random
import math
DELTA = 0.01 

class Problem:
    def __init__(self):
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self): # interface만 제공
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
        # super().__init__(self) 둘다 가능
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

    def getDelta(self): # 델타 리턴
        return self._delta
    
    def getAlpha(self): # 알파 리턴
        return self._alpha

    def getDx(self):    # dx 리턴
        return self._dx

    def takeStep(self, x, v):   # 기울기의 음의 방향으로 이동
        grad = self.gradient(x, v)  # 현재 위치에서의 기울기 계산
        xCopy = x[:] # 복사

        for i in range(len(xCopy)): # x길이 만큼 반복
            xCopy[i] -= self._alpha * grad[i]   # 기울기 음의 방향으로 이동 
        
        if self.isLegal(xCopy):  # 범위가 타당한지 확인 하기 
            return xCopy
        else:
            return x

    def gradient(self,x,v): # 해당부분에서의 기울기를 구한다.
        grad = []

        for i in range(len(x)):
            xCopyH = x[:]   # 복사
            xCopyH[i] += self._dx # x_에 dx를 더해준다. !
            g = (self.evaluate(xCopyH)-v)/self._dx  # 기울기 계산
            grad.append(g)  # 기울기 리스트에 추가 
        return grad # 리스트 반환

    def isLegal(self, x):   # low, up 추출
        domain = self._domain
        low = domain[1]
        up = domain[2]
        flag = True

        for i in range(len(low)): # x길이 만큼 돌면서 범위내에 있는지 확인
            if x[i] < low[i] or x[i] > up[i]:
                flag = False    # 범위 벗어나면?
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
    
    def randomMutant(self,current): ### TODO  # 공통인 함수는 아님.
        i = random.randint(0,len(current)-1)
        if random.uniform(0,1)>0.5: # 0.5 확률로 +,- 결정
            d = self.getDelta()    
        else:
            d = -self.getDelta()
        return self.mutate(current, i, d)  # +,- 방향으로 mutate 시킴. (객체 메서드 호출)

class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []       # A list of tuples
        self._distanceTable = []

    ### Tsp methods
    # tsp의 createProblem을 setVariables 메소드로 변경
    def setVariables(self):
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')  # 파일 경로 입력받기
        self._numCities = int(infile.readline())
        locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            locations.append(eval(line))  # 튜플 만들고 추가하고 읽고 닫기
            line = infile.readline()
        infile.close()
        self._locations = locations # 읽은 locations을 self._locations에 넣기
        self._distanceTable = self.calcDistanceTable()  # table 대신 self._distanceTable로 두기


    def calcDistanceTable(self):
        table = [[0] * self._numCities for _ in range(self._numCities)]

        for i in range(self._numCities):
            for j in range(self._numCities):
                if i != j:
                    distance = math.sqrt((self._locations[j][0] - self._locations[i][0]) ** 2 + (self._locations[j][1] - self._locations[i][1]) ** 2)
                    table[i][j] = distance

        return table

    def randomInit(self):
        n =self._numCities # p[0]은 numcitiest
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        self._numEval += 1  # Problem에있는 _numEval을 ++ 해주며 얼마나 많이 evalution 하는지 추척해준다.

        n = self._numCities    # p[0] 은 numcities
        table = self._distanceTable    # p[2] = distance table 임
        cost = 0    # 0에서부터 for 문을 돌면서 n-1만큼 sum 진행

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

    def inversion(self, current, i, j): # 파라미터만 바꿔준다.
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
        n = self._numCities # p[0] 은 self._numCities니까 변경하기
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations # p[1] 은 self._locations니까 변경하기
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def tenPerRow(self):   # 그대로 
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