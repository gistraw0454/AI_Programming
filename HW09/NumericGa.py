import random
import math

def main():
    p, alg = readPlanAndCreate()  # Setup and create (problem, algorithm)
    conductExperiment(p, alg)     # Conduct experiment & produce results
    p.describe()                  # Describe the problem solved
    alg.displayNumExp()           # Total number of experiments
    alg.displaySetting()          # Show the algorithm settings
    p.report()                    # Report result

def readPlanAndCreate():
    parameters = readValidPlan()  # Read and store in 'parameters'
    p = createProblem(parameters)
    alg = createOptimizer(parameters)
    return p, alg

def readValidPlan():  # Gradient Descent cannot solve TSP
    while True:
        parameters = { 'pType':1, 'pFileName':'problem/Ackley.txt', 'aType':6, 'delta':0.01,
                   'limitStuck':1000, 'alpha':0.01, 'dx':0.0001, 'numRestart':10,
                   'limitEval':100, 'popSize':10, 'resolution':10,'uXp':0.2,
                   'mrF':1,'XR':0.5,'mR':0.9, 'numExp':2 }
        if parameters['pType'] == 2 and parameters['aType'] == 4:   # 예외처리
            print("You cannot choose Gradient Descent")
            print("       unless your want a numerical optimization.")
        else:
            break
    return parameters


def createProblem(parameters): ### TODO (정답 !)
    pType = parameters['pType']
    if pType == 1:
        p = Numeric()
    # elif pType == 2:
    #     p = Tsp()
    # p.setVariables 함수 수정하기
    p.setVariables(parameters)
    return p

def createOptimizer(parameters): ### TODO (정답 !)
    optimizers = { 1: 'SteepestAscent()',
                    2: 'FirstChoice()',
                    3: 'Stochastic()',
                    4: 'GradientDescent()',
                    5: 'SimulatedAnnealing()',
                    6: 'GA()' }
    aType = parameters['aType']
    alg = eval(optimizers[aType])
    # alg.setVariables 함수 수정하기
    alg.setVariables(parameters)
    return alg

def conductExperiment(p, alg):
    aType = alg.getAType()
    if 1 <= aType <= 4:
        alg.randomRestart(p)
    else:
        alg.run(p)
    bestSolution = p.getSolution()
    bestMinimum = p.getValue()    # First result is current best
    numEval = p.getNumEval()
    sumOfMinimum = bestMinimum    # Prepare for averaging
    sumOfNumEval = numEval        # Prepare for averaging
    sumOfWhen = 0                 # When the best solution is found
    if 5 <= aType <= 6:
        sumOfWhen = alg.getWhenBestFound()
    numExp = alg.getNumExp()
    for i in range(1, numExp):
        if 1 <= aType <= 4:
            alg.randomRestart(p)
        else:
            alg.run(p)
        newSolution = p.getSolution()
        newMinimum = p.getValue()  # New result
        numEval = p.getNumEval()
        sumOfMinimum += newMinimum
        sumOfNumEval += numEval
        if 5 <= aType <= 6:
            sumOfWhen += alg.getWhenBestFound()
        if newMinimum < bestMinimum:
            bestSolution = newSolution  # Update the best-so-far
            bestMinimum = newMinimum
    avgMinimum = sumOfMinimum / numExp
    avgNumEval = round(sumOfNumEval / numExp)
    avgWhen = round(sumOfWhen / numExp)
    results = (bestSolution, bestMinimum, avgMinimum,
               avgNumEval, sumOfNumEval, avgWhen)
    p.storeExpResult(results)


############## Setup #################
class Setup:
    def __init__(self):
        self._pType = 0
        self._aType = 0
        self._delta = 0
        self._alpha = 0
        self._dx = 0
    def setVariables(self, parameters):
        self._pType = parameters['pType']
        self._aType = parameters['aType']
        self._delta = parameters['delta']
        self._alpha = parameters['alpha']
        self._dx = parameters['dx']
    def getAType(self):
        return self._aType
    

########### Problem ###############
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

    def getSolution(self):
        return self._solution
    
    def getValue(self):
        return self._value

    def getNumEval(self):
        return self._numEval
    
    def indToSol(self, ind):    # 복붙하기..? 여기 위치가 맞나 싶다.
        return self.decode(ind[1])



################## Numeric ##################
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
        print("Average number of evalutions: {0:,}".format(int(self._avgNumEval)))  # 평균 최소 평가 횟수 출력
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
        pop=[]
        for i in range(size):
            chromosome=self.randBinStr()
            pop.append([0, chromosome])
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
        chr1, chr2=self.uXover(ind1[1], ind2[1], uXp)
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
        n = len(ind[1])
        for i in range(len(child)):
            if random.uniform(0,1) <mrF * (1/n):
                child[1][i]= 1-child[1][i]
        return child


################# Optimizer ###################
class Optimizer(Setup): # Optimizer class interface

    def __init__(self):
        Setup.__init__(self)
        self._pType =0
        self._numExp = 1
        
    
    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pType = parameters['pType']
        self._numExp = parameters['numExp']
        

    def getNumExp(self):
        return self._numExp
    
    def displayNumExp(self):
        print(f"Number of experiments: {self._numExp}")

    def displaySetting(self):
        if self._pType == 1 and self._aType != 4 and self._aType != 6:
            print("Mutation step size:", self._delta)


#################### MetaHeuristic #######################
class MetaHeuristic(Optimizer): # Optimizer를 상속받는 MetaHeuristic class interface
    def __init__(self):
        Optimizer.__init__(self)    # super class의 생성자 호출
        self._limitEval =0
        self._whenBestFound =0

    def setVariables(self,parameters):
        Optimizer.setVariables(self, parameters)
        self._limitEval = parameters['limitEval']

    def getWhenBestFound(self):
        return self._whenBestFound
        
    def displaySetting(self):
        Optimizer.displaySetting(self)
        print("Number of evaluations until termination: {0:,}".format(self._limitEval))



############### GA #######################

class GA(MetaHeuristic):
    def __init__(self):
        MetaHeuristic.__init__(self)
        self._popSize = 0     # Population size
        self._uXp = 0   # Probability of swappping a locus for Xover
        self._mrF = 0   # Multiplication factor to 1/n for bit-flip mutation
        self._XR = 0    # Crossover rate for permutation code
        self._mR = 0    # Mutation rate for permutation code
        self._pC = 0    # Probability parameter for Xover
        self._pM = 0    # Probability parameter for mutation

    def setVariables(self, parameters):
        MetaHeuristic.setVariables(self, parameters)
        self._popSize = parameters['popSize']
        self._uXp = parameters['uXp']
        self._mrF = parameters['mrF']
        self._XR = parameters['XR']
        self._mR = parameters['mR']
        if self._pType == 1:
            self._pC = self._uXp
            self._pM = self._mrF
        if self._pType == 2:
            self._pC = self._XR
            self._pM = self._mR

    def displaySetting(self):
        print()
        print("Search Algorithm: Genetic Algorithm")
        print()
        MetaHeuristic.displaySetting(self)
        print()
        print("Population size:", self._popSize)
        if self._pType == 1:   # Numerical optimization
            # print("Number of bits for binary encoding:", self._resolution)
            print("Swap probability for uniform crossover:", self._uXp)
            print("Multiplication factor to 1/L for bit-flip mutation:",
                  self._mrF)
        elif self._pType == 2: # TSP
            print("Crossover rate:", self._XR)
            print("Mutation rate:", self._mR)


    def evalAndFindBest(self, pop, p):
        best = pop[0]
        p.evalInd(best)
        bestValue = best[0]
        for i in range(1, len(pop)):
            p.evalInd(pop[i])
            newValue = pop[i][0]
            if newValue < bestValue:
                best = pop[i]
                bestValue = newValue
        return best
    
    def run(self, p):
        # Population 생성
        pop = p.initializePop(self._popSize)
        # Population 중 최적해 찾기
        best = self.evalAndFindBest(pop, p)
        numEval = p.getNumEval()
        whenBestFound = numEval
        # limitEval 까지 [다음세대 생성–평가] 반복
        while numEval < self._limitEval:
            # print(f"Current Evaluations: {numEval}, Limit: {self._limitEval}")  # 디버깅
            newPop = []
            I = 0
            # 다음 세대 생성; start
            while I < self._popSize:
                par1, par2 = self.selectParents(pop)
                ch1, ch2 = p.crossover(par1, par2, self._pC)
                newPop.extend([ch1, ch2])
                I += 2

            # 돌연변이 적용
            newPop = [p.mutation(ind, self._pM) for ind in newPop]
            pop = newPop
            # 다음 세대 값 평가 및 best 업데이트
            newBest = self.evalAndFindBest(pop, p)
            numEval = p.getNumEval()  # 평가 횟수 업데이트
            if newBest[0] < best[0]:
                best = newBest
                whenBestFound = numEval

        self._whenBestFound = whenBestFound
        bestSolution = p.indToSol(best)
        p.storeResult(bestSolution, best[0])


    def selectParents(self, pop):
        ind1, ind2=self.selectTwo(pop)
        par1 =self.binaryTournament(ind1, ind2)
        ind1, ind2=self.selectTwo(pop)
        par2 =self.binaryTournament(ind1, ind2)
        return par1, par2

    def selectTwo(self, pop):   ### TODO 
    # pop에서 random하게 2개의 individuals 선택해서 반환 (단순 비교문)
        popCopy = pop[:]
        random.shuffle(popCopy)
        return popCopy[0],popCopy[1]    

    def binaryTournament(self, ind1, ind2): ### TODO 
    # 2개의 individuals 중 더 좋은 ind선택해서 반환 (랜덤)
        if ind1[0] < ind2[0] : return ind1 #ind1[0]에 값이 들어있을거기때문..
        else : return ind2

    

main()