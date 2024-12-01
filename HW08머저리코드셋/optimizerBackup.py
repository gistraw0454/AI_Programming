from setup import Setup

class Optimizer(Setup):
    def __init__(self):
        Setup.__init__(self)

class MetaHeuristic(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)

class SimulatedAnnealing(MetaHeuristic):
    def __init__(self):
        MetaHeuristic.__init__(self)

class Stochastic(HillClimbing):
    def __init__(self):
        pass
    
    def displaySetting(self):
        print()
        print("Search Algorithm: Stochastic Hill Climbing")
        print()
        HillClimbing.displaySetting(self)
    
    def run(self,p):
        # hint; Stochastic 알고리즘은 Steepest Ascent 알고리즘과 흐름이 유사
        current = p.randomInit()    # 랜덤한 current 결정
        valueC = p.evaluate(current)    # 현재의 evaluation 계산
        i = 0
        while i < self._limitStuck:  # limit 만큼 돌면서 새 solution을 찾을 때까지 계속 돌아준다.
            neighbors = p.mutants(current)
            successor,valueS = self.stochasticBest(neighbors,p)
            if valueS < valueC: # new solution이 더 좋으면 바꿔준다. <- 반복
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.storeResult(current, valueC)

    def stochasticBest(self, neighbor):
        def __init__(self):
            pass

class HillClimbing(Optimizer):
    def __init__(self):
        ...
        self._numRestart = 1    # 이거 1번 10번 비교해보기
        ...

    def randomRestart(self,p):
        i=1
        self.run(p)
        bestSolution = p.getSolition()
        bestMinimum = p.getValue()
        numEval = p.getNumEval()
        while i < self._numRestart:
            self.run(p)
            newSolution = p.getSolition()
            newMinimum = p.getValue()
            numEval += p.getNumEval()
            if newMinimum < bestMinimum:
                bestSolition = newSolution
                bestMinimum = newMinimum
            i+=1
        
        p.storeResult(bestSolition,bestMinimum)

class HillClimbing(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0 # 1: Numeric, 2 : Tsp
        self._limitStuck = 100

    def setVariables(self, pType):
        # 1. pType을 인자로 받아서 self._pType에 assign
        self._pType = pType

    def displaySetting(self):
        # 1. pType==1 (Numeric) 일 때만, Mutation step size를 출력하는 함수
        # first-choice.py 코드의 ‘print(＂Mutation step size:＂, p.getDelta())’ 부분 활용
        if (self._pType == 1):  
            print()
            print("Mutation step size:", self._delta)
   
    def run(self):
        pass

class FirstChoice(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        super().displaySetting()    # HillClimbing.displaySetting(self) 도 가능
        print("Max evaluations with no improvement: {0:,} iterations".format(self._limitStuck))
    
    def run(self,p):
        current = p.randomInit()    # 랜덤한 current 결정
        valueC = p.evaluate(current)    # 현재의 evaluation 계산
        i = 0
        while i < self._limitStuck:  # limit 만큼 돌면서 새 solution을 찾을 때까지 계속 돌아준다.
            successor = p.randomMutant(current) # randMutant로 랜덤하게 변형하여 solution을 만든다.
            valueS = p.evaluate(successor)  # 그 솔루션의 evalution을 계산한다.
            if valueS < valueC: # new solution이 더 좋으면 바꿔준다. <- 반복
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.storeResult(current, valueC)


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

class SimulatedAnnealing(MetaHeuristic):
    def __init__(self):
        self._numSample=100
        self._limitEval=100000
        self._whenBestFound=0

    def displaySetting(self):
        print("Search Algorithm: Simulated Annealing")
        print("Number of evaluations until termination: {0:,}".format(self._limitEval))
    
    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        best, valueBest = current, valueC
        whenBestFound = i=1
        t = self.initTemp(p) 
        while True:
            ... # Implement
        self._whenBestFound=whenBestFound
        p.storeResult(best, valueBest)
    
    def stochasticBest(self, neighbors, p):
        # Smaller valuse are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]

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