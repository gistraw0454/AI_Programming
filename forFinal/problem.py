import random
import math
from setup import Setup

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
    
class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []       # A list of tuples
        self._distanceTable = []

    def calcDistanceTable(self):    ### TODO
        table = [[0]*self._numCities for _ in range(self._numCities)]   # n*n 배열 만들기

        for i in range(self._numCities):
            for j in range(self._numCities):
                if i != j:
                    distance = math.sqrt((self._locations[j][0]-self._locations[i][0])**2 + (self._locations[j][1]-self._locations[i][1])**2)
                    table[i][j] = distance
        return table
    
    # 평가함수 : current의 total cost구하기
    def evaluate(self,current): ### TODO current = [24,31,25,8,7,15] 경로 list
        self._numEval += 1
        n = self._numCities
        table = self._distanceTable
        cost = 0

        for i in range(n-1):
            locFrom = current[i]
            locTo = current[i+1]
            cost += table[locFrom][locTo]

        cost += table[current[-1]][current[0]]  # 끝과 처음을 이어준다.
        return cost
    
    def mutants(self, current): # 가능한 여러 이웃만들기
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:
            i,j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i,j] not in triedPairs:   # 이전에 시도한적 없을 경우에만 진행 (중복 방지)
                triedPairs.append([i,j])    # 시도했다고 저장해서 표시
                curCopy = self.inversion(current, i, j) # 단순 inversion으로 새 이웃 만든다.
                count += 1
                neighbors.append(curCopy)
        return neighbors

    def inversion(self, current, i, j):
        curCopy = current[:]
        while i < j:
            curCopy[i],curCopy[j] = curCopy[j],curCopy[i]
            i +=1
            j -=1
        return curCopy
        
    def randomMutant(self, current):
        while True:
            i,j = sorted([random.randrange(self._numCities) for _ in range(2)]) # randrange(n) 0~n수를 2번 뽑아 [1,3] 만든다.
            if i<j:
                curCopy = self.inversion(current,i,j)   # current에서 i부터 j까지 구간 반전을해서 새로운 이웃을 만든다.
                break
        return curCopy

    def randomInit(self):
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init
    
    
    

