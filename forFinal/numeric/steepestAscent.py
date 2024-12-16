import random
import math

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

class Optimizer(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._numExp = 1

    def setVariables(self, parameters):
        super().setVariables(parameters)
        # Setup.setVariables(self,parameters)
        self._numExp = parameters['numExp']

    def getNumExp(self):
        return self._numExp
    
    def displayNumExp(self):
        print("number of experiments: {}".format(self._numExp))

    def displaySetting(self):
        if self._pType == 1 and self._aType != 4 and self._aType != 6:  # numeric문제 중 gradientDescent, GA에는 mutaion step size가 필요없다.
            print("mutaion step size: ", self._delta)
    
class MetaHeuristic(Optimizer): 
    # For SimulatedAnnealing & GA
    
    # SimulatedAnnealing : T가 0이될때까지 줄여가면서, 전역적으로 bad move까지 허용하는거다.
    # next = 임의의 state; next-current < 0 이면, current = next; 아니면, e^(-(next-current)/T) 확률로 current = next;해준다.

    # GA : 자연선택설
    # population 수 만큼 돌면서, 각 객체의 fitness를 계산; fitnessRate로 두 부모를 뽑기; 
    # crossover로 자식만들기; mutationRate로 자식돌연변이; new_popultaion[i] = 자식;
    # 객체군이 유사해지거나, 시간이 많이 지날때까지 loop 돌면서 다음세대로 물려주기.
     
    def __init__(self):
        Optimizer.__init__(self)
        self._limitEval = 0 # 둘다 전역적으로 돌기때문에 limitEval가 필요하다.
        self._whenBestFound = 0

    def setVariables(self,parameters):
        Optimizer.setVariables(self,parameters)
        self._limitEval = parameters['limitEval']

    def getWhenBestFound(self):
        return self._whenBestFound

    def displaySetting(self):
        super().displaySetting()
        print("Number of total eval: {}".format(self._limitEval))

class SimulatedAnnealing(MetaHeuristic):
    def __init__(self):
        MetaHeuristic.__init__(self)
        self._numSample = 100
    
    def displaySetting(self):
        print("Search Algorithm: Simulated Annealing")
        return super().displaySetting()
    
    def run(self,p):    # problem을 가져와서 돌린다.
        current = p.randomInit()    # 임의로 current를 정한다.
        valueC = p.evaluate(current)    # 현재 상태를 평가하는 평가 함수
        # f= open('anneal.txt','w')
        best, valueBest = current, valueC
        whenBestFound = 1
        i = 1
        t = self.initTemp(p)
        
        while True:
            t = self.tSchedule(t)   # Annealing Schedule[t]로 t가 감소한다.
            if t==0 or i == self._limitEval:
                break

            next = p.randomMutant(current)  # 현재 상태에 대한 randomMutant(이웃) 생성
            valueN = p.evaluate(next)
            dE = valueN - valueC

            if (dE < 0):
                current = next
                valueC = valueN
            else:
                if random.uniform(0,1) < math.exp(-dE/t):   # 해당확률에 따라 bad move 수행
                    current = next
                    valueC = valueN

            # f.write(str(valueC)+'\n')
            if valueC < valueBest:
                best, valueBest = current, valueC
                whenBestFound = i 

        self._whenBestFound = whenBestFound
        p.storeResult(best,valueBest)
        # f.close()

    def initTemp(self,p):   # 온도를 초기화한다.
        diffs = []
        
    
    def tSchedule(t):
        return t * (1-(1/10**4))    # t*(9999/10000)



    

    


