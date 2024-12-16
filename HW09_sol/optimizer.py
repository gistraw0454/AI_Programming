from setup import Setup
import random
import math

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


class  HillClimbing(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)
        self._pType = 0
        self._limitStuck = 100
        self._numRestart = 5    # 반복횟수 설정 

    def setVariables(self, parameters): 
        # 1. pType을 인자로 받아서 self._pType에 assign
        Optimizer.setVariables(self,parameters)
        self._limitStuck = parameters['limitStuck']
        self._numRestart = parameters['numRestart']

    def displaySetting(self):
        # 1. pType==1 (Numeric) 일 때만, Mutation step size를 출력하는 함수
        # first-choice.py 코드의 ‘print(＂Mutation step size:＂, p.getDelta())’ 부분 활용
        if self._pType == 1:
            print()
            print("Mutation step size:", self._delta)

    def run(self):
        pass

    def randomRestart(self, p):         
        i = self._numRestart
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()
        numEval = p.getNumEval()

        while i < self._numRestart:
            self.run(p)
            i += 1

            newSolution = p.getSolution()
            newMinimum = p.getValue()
            numEval += p.getNumEval()

            if newMinimum < bestMinimum:
                bestSolution = newSolution
                bestMinimum = newMinimum


        p.storeResult(bestSolution, bestMinimum)

class Stochastic(HillClimbing): # HillClimbing 상속받는 Stochastic class
    def __init__(self):
        HillClimbing.__init__(self) # super class의 생성자 호출

    def displaySetting(self): 
        print()
        print("Search Algorithm: Stochastic Hill Climbing") # 추가로 호출할 부분
        print()
        HillClimbing.displaySetting(self)   # super class의 해당 메서드 호출

    def run(self, p):   # 실행 메서드
        current = p.randomInit()  
        valueC = p.evaluate(current)
        f = open('stochastic.txt','w')  # stochastic.txt 파일 열기
        i = 0

        while i < self._limitStuck:
            neighbors = p.mutants(current)
            temp, valueS = self.stochasticBest(neighbors, p)    # 호출하는 함수가 Steepest와 다름 (나머지는 유사)
            f.write(str(valueC)+'\n')   # 파일에 한줄 씩 작성 ( 매 iteration 마다 결과를 저장 )

            if valueS < valueC:
                current = temp
                valueC = valueS
                i = 0 

            else:
                i += 1

        p.storeResult(current, valueC)
        f.close()   # f 닫기

    def stochasticBest(self, neighbors, p): # 예제 코드 가져옴
        valuesMin = [p.evaluate(indiv) for indiv in neighbors]
        large = max(valuesMin) + 1
        valuesMax = [large - val for val in valuesMin]

        total = sum(valuesMax)
        randValue = random.uniform(0, total)
        s = valuesMax[0]

        for i in range(len(valuesMax)):
            if randValue <= s: 
                break
            else:
                s += valuesMax[i+1]

        nextSolution=neighbors[i]
        nextValue=valuesMin[i]
        return nextSolution, nextValue

class FirstChoice(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        print()
        super().displaySetting()    # HillClimbing.displaySetting(self) 도 가능
        print("Max evaluations with no improvement: {0:,} iterations".format(self._limitStuck))
        print()

    def run(self,p):
        current = p.randomInit()    # 랜덤한 current 결정
        valueC = p.evaluate(current)    # 현재의 evaluation 계산
        f = open('first.txt','w')
        i = 0
        while i < self._limitStuck:  # limit 만큼 돌면서 새 solution을 찾을 때까지 계속 돌아준다.
            successor = p.randomMutant(current) # randMutant로 랜덤하게 변형하여 solution을 만든다.
            valueS = p.evaluate(successor)  # 그 솔루션의 evalution을 계산한다.
            f.write(str(valueC)+'\n')
            if valueS < valueC: # new solution이 더 좋으면 바꿔준다. <- 반복
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.storeResult(current, valueC)
        f.close()

class SteepestAscent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        super().displaySetting()

    def run(self,p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors,p)    # self.
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current,valueC)
    
    def bestOf(self,neighbors, p): # self, 추가
        best = neighbors[0]
        bestValue = p.evaluate(best)
        
        for neighbor in neighbors[1:]:
            value = p.evaluate(neighbor)
            if value < bestValue:
                best = neighbor
                bestValue = value
        return best, bestValue

class GradientDescent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: Gradient Descent")
        print()
        print("Udate rate:", self._alpha)
        print("Increment for calculating derivative:", self._dx)
    
    def run(self,p):
        currentP = p.randomInit()  # Current point
        valueC = p.evaluate(currentP)
        while True:
            nextP = p.takeStep(currentP, valueC)
            valueN = p.evaluate(nextP)
            if valueN >= valueC:
                break
            else:
                currentP = nextP
                valueC = valueN
        p.storeResult(currentP, valueC)


###################### SimulatedAnnealing ################33
class SimulatedAnnealing(MetaHeuristic):
    def __init__(self):
        MetaHeuristic.__init__(self) 
        self._numSample=100

    def displaySetting(self):
        print("Search Algorithm: Simulated Annealing")
        MetaHeuristic.displaySetting(self)
        print()
        
    
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        f= open('anneal.txt','w')
        best, valueBest = current, valueC
        whenBestFound = 1
        i = 1
        t = self.initTemp(p) 

        while True:
            # 1. tSchedule을 통해 t update
            t = self.tSchedule(t)   # 온도 감소
            if t==0 or i == self._limitEval:
                break

            # 2. 현재 상태에 대한 randomMutant 생성
            neighbor = p.randomMutant(current)
            valueN = p.evaluate(neighbor)
            i+=1
            dE = valueN - valueC
            
            if dE < 0:
                current = neighbor
                valueC = valueN
            elif random.uniform(0,1)< math.exp(-dE/t):
                current = neighbor
                valueC = valueN

            f.write(str(valueC)+'\n')

            if valueC < valueBest:
                best, valueBest = current, valueC
                whenBestFound = i
    
        self._whenBestFound = whenBestFound
        p.storeResult(best, valueBest)
        f.close()
    
    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t

    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))

class GA(MetaHeuristic):
    def __init__(self): # 스켈레톤 코드 복사 
        MetaHeuristic.__init__(self)
        self._popSize = 0     # Population size
        self._uXp = 0   # Probability of swappping a locus for Xover
        self._mrF = 0   # Multiplication factor to 1/n for bit-flip mutation
        self._XR = 0    # Crossover rate for permutation code
        self._mR = 0    # Mutation rate for permutation code
        self._pC = 0    # Probability parameter for Xover
        self._pM = 0    # Probability parameter for mutation

    def setVariables(self, parameters): # 스켈레톤 코드 복사 
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

    def displaySetting(self):   # 스켈레톤 코드 복사 
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
    
    def run(self, p):   
        # Population 생성
        pop = p.initializePop(self._popSize)    # popsize만큼 초기화
        # Population 중 최적해 찾기
        best = self.evalAndFindBest(pop, p) # pop 내에서 최적해를 eval하고 best담음
        numEval = p.getNumEval()    # 현재 numeval
        whenBestFound = numEval # 최적해 발견한 numeval 기록 (best..)
        # limitEval 까지 [다음세대 생성–평가] 반복
        while numEval < self._limitEval:
            # print(f"Current Evaluations: {numEval}, Limit: {self._limitEval}")  # 디버깅
            newPop = [] # 새 population [] 생성 (자손?)
            I = 0   
            # 다음 세대 생성; start
            while I < self._popSize:    # popSize만큼 계속 돈다.
                par1, par2 = self.selectParents(pop)    # 두 부모를 선택하고
                ch1, ch2 = p.crossover(par1, par2, self._pC)    # crossover해준다.
                newPop.extend([ch1, ch2])   # 생성된 자식을 newPop에 추가
                I += 2  # 2명 늚

            # 돌연변이 적용 (mutation)
            newPop = [p.mutation(ind, self._pM) for ind in newPop]  # 자식 pop에서 각 객체에 pM확률로 mutation 시킨다. (돌연변이) 
            pop = newPop    # 자식세대를 현재세대로 업데이트
            # 다음 세대 값 평가 및 best 업데이트   
            newBest = self.evalAndFindBest(pop, p)
            numEval = p.getNumEval()  # 평가 횟수 업데이트
            if newBest[0] < best[0]:    # 최적해가 이전보다 좋으면 업데이트
                best = newBest  #값
                whenBestFound = numEval #numEval

        self._whenBestFound = whenBestFound 
        bestSolution = p.indToSol(best) # 최적해를 해석가능한 sol로 변환하기
        p.storeResult(bestSolution, best[0])    # 값 저장

    def evalAndFindBest(self, pop, p):  
            best = pop[0]   
            p.evalInd(best) # 염색체 eval하기
            bestValue = best[0] # 잘난놈
            for i in range(1, len(pop)):       # pop len만큼 돌면서 좋은거 찾기
                p.evalInd(pop[i])
                newValue = pop[i][0]
                if newValue < bestValue:    # 더잘난게 있으면 바꿔주기
                    best = pop[i]   
                    bestValue = newValue
            return best # 잘난놈 return 

    def selectParents(self, pop):
        ind1, ind2=self.selectTwo(pop)  # pop중 개체 둘을 뽑고 더 우수한 개체를 부모로 삼는다.
        par1 =self.binaryTournament(ind1, ind2) # 우수한 개체 뽑기
        ind1, ind2=self.selectTwo(pop)  # pop중 개체 둘을 뽑고 더 우수한 개체를 부모로 삼는다.
        par2 =self.binaryTournament(ind1, ind2) # 우수한 개체 뽑기
        return par1, par2 #우수한 둘을 부모로 리턴 

    def selectTwo(self, pop):   ### TODO 
    # pop에서 random하게 2개의 individuals 선택해서 반환 (단순 비교문)
        popCopy = pop[:]    # pop copy
        random.shuffle(popCopy) # 섞어
        return popCopy[0],popCopy[1]   # 앞에 두개 뽑아 (그냥 암거나 두개 뽑는거임)  

    def binaryTournament(self, ind1, ind2): ### TODO 
    # 2개의 individuals 중 더 좋은 ind선택해서 반환 (랜덤)
        if ind1[0] < ind2[0] : return ind1 #ind1[0]에 값이 들어있을거기때문..
        else : return ind2

    






