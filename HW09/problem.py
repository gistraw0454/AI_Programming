from setup import Setup
import random
import math

class Problem(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._solution = []
        self._value = 0
        self._numEval = 0

        self._pFileName = ''
        self._bestSolution = []
        self._bestMinimum = 0
        self._avgMinimum = 0
        self._avgNumEval = 0
        self._sumOfNumEval = 0
        self._avgWhen = 0

    def setVariables(self, parameters): 
        Setup.setVariables(self, parameters)
        self._pFileName = parameters['pFileName']
    
    def storeExpResult(self, results):  # 결과값들 저장
        self._bestSolution = results[0]
        self._bestMinimum = results[1]
        self._avgMinimum = results[2]
        self._avgNumEval = results[3]
        self._sumOfNumEval = results[4]
        self._avgWhen = results[5]

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
        print("Total number of evaluations: {0:,}".format(self._sumOfNumEval))

    def avgReport(self):
        if 1<= self._aType <=4:
            print("Average number of evaluations: {0:,}".format(round(self._avgNumEval)))
        if 5<= self._aType <=6:
            print("Average iteration of finding the best: {0:,}".format(self._avgWhen))

    def getSolution(self):
        return self._solution
    
    def getValue(self):
        return self._value

    def getNumEval(self):
        return self._numEval
    
    


class Numeric(Problem): ###TODO 실습 : 여기에 InitializePop 구현하기
    def __init__(self):
        Problem.__init__(self)
        # super().__init__(self) 둘다 가능
        self._expression = ''
        self._domain = []     # domain as a list
        self._resolution = 0

    def setVariables(self,parameters):
        Problem.setVariables(self,parameters)
        fileName = self._pFileName
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
        self._resolution = parameters['resolution']
        

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

        print("Average objective value: {0:,.3f}".format(self._avgMinimum))    # 평균 최소값 출력
        Problem.avgReport(self)
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Best value: {0:,.3f}".format(self._bestMinimum))
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
    

    def initializePop(self, size): 
        pop=[]  # 빈 pop (현)
        for i in range(size):   # 파라미터 size만큼 돌면서
            chromosome=self.randBinStr()    # 랜덤한 bin 문자열 만들기
            pop.append([0, chromosome]) # 평가값, 염색체들 뽑기
        return pop
    
    def randBinStr(self):
        # Numeric 문제의 변수 N (self._domain[0]) 개에 대해서,
        k = len(self._domain[0])*self._resolution
        # 각 변수 별 self._resolution크기의 random binary 생성
        # N=5, self._resolution=10 이라면, 
        chromosome = []
        for i in range(k):
            allele = random.randint(0,1)
            chromosome.append(allele)
        # 50길이의 [1, 0, 1, 0, 0, 1, 0, 1, …] 배열 생성하여 반환
        return chromosome   # population의 초기단계
    

    ### 복사했음
    def evalInd(self, ind): 
        ind[0] = self.evaluate(self.decode(ind[1]))
    ### 복사했음
    def decode(self, chromosome):
        r = self._resolution
        low = self._domain[1] 
        up = self._domain[2] 
        genotype = chromosome[:]
        phenotype = []
        start = 0
        end = r
        for var in range(len(self._domain[0])): 
            value = self.binaryToDecimal(genotype[start:end],   
            low[var], up[var])
            phenotype.append(value)
            start += r
            end += r
        return phenotype
    
    ### TODO 이게 적어야하는거.
    def binaryToDecimal(self,binCode,l,u):
        r = len(binCode)
        decimalValue = 0
        for i in range(r):
            decimalValue += binCode[i] * (2**(r-1-i))
        return l + (u-l) * decimalValue/2**r
    

    def crossover(self, ind1, ind2, uXp):  
        chr1, chr2=self.uXover(ind1[1], ind2[1], uXp)   #uXp로 crossover시키기
        return[0, chr1], [0, chr2]

    def uXover(self, chrInd1, chrInd2, uXp): # uniform crossover
        # chrInd1, chrInd2의 각 원소를 확률적(uXp)으로 crossover 
        chr1 =chrInd1[:] # Make copies
        chr2 =chrInd2[:]
        # implement ### TODO
        for i in range(len(chr1)):
            if random.uniform(0,1) <uXp:
                chr1[i],chr2[i] = chr2[i],chr2[i]
        return chr1, chr2

    def mutation(self, ind, mrF): # bit-flip mutation
        # mrF * (1/ lnegth of individual) 확률로 ind의 개별 원소 bit-flip
        child = ind[:] # Make copy
        # implement ### TODO
        n = len(ind[1]) # 염색체 길이를 가져와
        for i in range(len(child)): # child만큼 돌리면서
            if random.uniform(0,1) <mrF * (1/n): # 계산
                child[1][i]= 1-child[1][i]
        return child
    
    def indToSol(self, ind):    # 복붙하기..? 여기 위치가 맞나 싶다.
        return self.decode(ind[1])  # decode해주기

class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []       # A list of tuples
        self._distanceTable = []

    ### Tsp methods
    # tsp의 createProblem을 setVariables 메소드로 변경
    def setVariables(self,parameters):
        Problem.setVariables(self,parameters)
        fileName = self._pFileName
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
        print("Average tour cost: {0:,}".format(round(self._avgMinimum)))  # 평균 여행 비용 출력
        Problem.avgReport(self)
        print()
        print("Best order of visits:")
        self.tenPerRow()
        print("Best tour cost: {0:,}".format(round(self._bestMinimum)))   
        super().report()

    def initializePop(self,size):   ### TODO 초기 자식 생성
        pop = []    
        for i in range(size):   # 파라미터 size만큼 돌면서 
            chromosome = self.randomInit()   # tsp.randomInit메서드 이용하여 chromosome 생성하고 pop에 추가
            pop.append([0,chromosome])     # 초기 평가값은 0으로하고 나머지는 랜덤으로 하여 pop에 추가
        return pop
    
    def evalInd(self, ind):     # 한 개체의[1] 평가값을 계산하여 ind[0]에 저장한다.
        ind[0] = self.evaluate(ind[1])

    def crossover(self, ind1, ind2, XR):   #chromosome = [eval_value, [tour order]] = [0, [5, 12, 17, 11, 7, 22, …]]
        if random.uniform(0, 1) <= XR:  # 교차확률 XR에 따라서 oXover 교차를 한다.
            chr1, chr2 = self.oXover(ind1[1], ind2[1])
        else:
            chr1, chr2 = ind1[1][:], ind2[1][:] # 그대로 
        return [0, chr1], [0, chr2]

    def oXover(self, chr1, chr2):   ### TODO : ppt 참고 구현하기 ! 찐 교차
        # 1. Ind 길이 사이의 두 값 a, b 생성 (a < b)
        a, b = sorted(random.sample(range(len(chr1)  ), 2))  # [a,b]중 하나를 골라 무작위로 추출
        
        # 2. chr1과 chr2의 a~b 구간 대응하는 원소 찾기
        a_b_chr1 = chr1[a:b + 1]    
        a_b_chr2 = chr2[a:b + 1]
        
        # 3. 사이 값과 같은 값을 상대 individual에서 삭제
        rmv_chr1 = []  # 빈 리스트를 생성
        for gene in chr2:  # chr2 리스트의 각 요소(유전자)에 대해 반복
            if gene not in a_b_chr1:  # 만약 그 유전자가 a_b_chr1에 없다면
                rmv_chr1.append(gene)  # 그 유전자를 rmv_chr1 리스트에 추가
        rmv_chr2 = []  # 빈 리스트를 생성
        for gene in chr1:  # chr1 리스트의 각 요소(유전자)에 대해 반복
            if gene not in a_b_chr2:  # 만약 그 유전자가 a_b_chr2에 없다면
                rmv_chr2.append(gene)  # 그 유전자를 rmv_chr2 리스트에 추가
        
        # 4. 왼쪽에서부터 남은 값을 shift하며 비워진 구간 채우기
        new_chr1 = rmv_chr1[:a] + a_b_chr1 + rmv_chr1[a:]
        new_chr2 = rmv_chr2[:a] + a_b_chr2 + rmv_chr2[a:]
        
        return new_chr1, new_chr2

    def mutation(self, ind, mR):    # TODO : 주석 참고 구현하기 !
        # mR 확률로 mutation 수행
        if random.uniform(0, 1) <= mR:  # mR 변이확률에 따라 변이시키기
            chromosome = ind[1] # ind[1]염색체를 가져와서 길이를 가져와
            length = len(chromosome)
            # 1. 두 값 i, j (i < j) 생성
            i, j = sorted(random.sample(range(length), 2))  # 해당길이부터 2까지 무작위로 i,j를 뽑고 
            
            # 2. i~j 구간 inversion 수행 반전 시킨다.
            chromosome[i:j + 1] = reversed(chromosome[i:j + 1])
        
        return ind

    def indToSol(self, ind):
        return ind[1]
