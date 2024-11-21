from setup import Setup

class HillClimbing(Setup):
    def __init__(self):
        # 1. Setup에 정의된 delta, alpha, dx에 접근하기 위해 Setup 초기화
        Setup.__init__(self)
        # 2. self._pType 정의하기 (Tsp인지, Numeric인지 구분하기 위한 Integer 변수 선언)
        self._pType = 0 # 1: Numeric, 2 : Tsp
        # 3. self._limitStuck 정의하기 (지금은 First-choice에서만 사용하지만, 앞으로 추가될 
        # 다른 hillclimbing 알고리즘에서 사용함)
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