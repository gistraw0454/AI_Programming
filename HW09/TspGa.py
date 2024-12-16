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
        parameters = { 'pType':2, 'pFileName':'HW09/problem/Tsp100.txt', 'aType':6, 'delta':0.01,
                   'limitStuck':50000, 'alpha':0.01, 'dx':0.0001, 'numRestart':10,
                   'limitEval':50000, 'popSize':10, 'resolution':10,'uXp':0.2,
                   'mrF':1,'XR':0.1,'mR':0.9, 'numExp':10 }
        if parameters['pType'] == 2 and parameters['aType'] == 4:   # 예외처리
            print("You cannot choose Gradient Descent")
            print("       unless your want a numerical optimization.")
        else:
            break
    return parameters


def createProblem(parameters): ### TODO (정답 !)
    pType = parameters['pType']
    # if pType == 1:
    #     p = Numeric()
    if pType == 2:
        p = Tsp()
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


############### Setup ###############
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

############## Problem ################
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
    



###################### Tsp ###################
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

    def initializePop(self,size):   ### TODO 
        n = self._numCities
        pop = []
        for i in range(size):
            chromosome = self.randomInit()   # tsp.randomInit메서드 이용하여 chromosome 생성하고 pop에 추가
            pop.append([0,chromosome])     #
        return pop
    
    def evalInd(self, ind): 
        ind[0] = self.evaluate(ind[1])

    def crossover(self, ind1, ind2, XR):   #chromosome = [eval_value, [tour order]] = [0, [5, 12, 17, 11, 7, 22, …]]
        if random.uniform(0, 1) <= XR:
            chr1, chr2 = self.oXover(ind1[1], ind2[1])
        else:
            chr1, chr2 = ind1[1][:], ind2[1][:] 
        return [0, chr1], [0, chr2]

    def oXover(self, chr1, chr2):   ### TODO : ppt 참고 구현하기 !
        # 1. Ind 길이 사이의 두 값 a, b 생성 (a < b)
        length = len(chr1)
        a, b = sorted(random.sample(range(length), 2))
        
        # 2. chr1과 chr2의 a~b 구간 추출
        segment1 = chr1[a:b + 1]
        segment2 = chr2[a:b + 1]
        
        # 3. chr2에서 chr1 segment와 겹치는 값 제거
        temp1 = [gene for gene in chr2 if gene not in segment1]
        temp2 = [gene for gene in chr1 if gene not in segment2]
        
        # 4. 왼쪽에서부터 남은 값을 shift하며 비워진 구간 채우기
        new_chr1 = temp1[:a] + segment1 + temp1[a:]
        new_chr2 = temp2[:a] + segment2 + temp2[a:]
        
        return new_chr1, new_chr2

    def mutation(self, ind, mR):    # TODO : 주석 참고 구현하기 !
        # mR 확률로 mutation 수행
        if random.uniform(0, 1) <= mR:
            chromosome = ind[1]
            length = len(chromosome)
            # 1. 두 값 i, j (i < j) 생성
            i, j = sorted(random.sample(range(length), 2))
            
            # 2. i~j 구간 inversion 수행
            chromosome[i:j + 1] = reversed(chromosome[i:j + 1])
        
        return ind

    def indToSol(self, ind):
        return ind[1]

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

        print()
        


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