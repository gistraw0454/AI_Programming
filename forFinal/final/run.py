import random

## Numeric(Problem):
class Numeric(Problem):
    ...
    def randomInit(self):
        domain = self._domain
        low, up = domain[1],domain[2]
        init= []

        for i in range(len(low)):
            r = random.uniform(low[i],up[i])
            init.append(r)
        return init

    # 새위치로 이동하거나 범위를 벗어난 경우 기존위치를 유지지
    def takeStep(self,x,valueC): # x = x - a*f'(x) a는 step크기. update rate임.
        grad = self.gradient(x,valueC)    # 현재 위치에서 기울기 계산
        xCopy = x[:]
        for i in range(len(xCopy)):
            xCopy -= self._alpha*grad[i]
        
        if self.isLegal(xCopy): # 전부 범위내에 있으면, xCopy 리턴
            return xCopy
        else:
            return x    # 범위 벗어나면 그냥 원래꺼 리턴    
    
    def gradient(self, x, v):
        grad=[]
        for i in range(len(x)):
            xCopyH = x[:]
            xCopyH[i] += self._dx
            g = (self.evaluate(xCopyH)-v)/self._dx
            grad.append(g)
        return grad
    
    def isLegal(self,x):
        domain = self._domain
        low = domain[1]
        up = domain[2]
        flag = True
        for i in range(len(low)):
            if x[i] <low[i] or x[i]>up[i]:
                flag = False
                break
        return flag





## TSP(Problem)
class Tsp(Problem):
    ...
    def randomInit(self):
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self,current): # current = [23,12,53,11]
        self._numEval += 1
        n = self._numCities
        table = self._distanceTable
        cost = 0

        for i in range(n-1):
            locFrom = current[i]
            locTo = current[i+1]
            cost += table[locFrom][locTo]
        
        cost += table[current[-1]][current[0]]
        return cost

    def randomMutant(self, current):
        while True: # inversion하려면 i,j가 다른값이 나와야하므로, 나올때까지 돌림림
            i,j = sorted([random.randrange(self._numCities) for _ in range(2)]) # randrange(n) 0~n수를 2번 뽑아 [1,3] 만든다.
            if i<j:
                curCopy = self.inversion(current,i,j)   # current에서 i부터 j까지 구간 반전을해서 새로운 이웃을 만든다.
                break
        return curCopy

    def mutants(self,current):
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []

        while count <= n:   # 총 도시수 만큼 이웃을 뽑는다
            i,j = sorted([random.randrange(n) for _ in range(2)])
            if i<j and [i,j] not in triedPairs:
                triedPairs.append([i,j])
                curCopy = self.inversion(current,i,j)
                count += 1  # i<j이고 중복아니여야지 count++
                neighbors.append(curCopy)
        return neighbors
    
## FirstChoice(HillClimbing) : 좋은거 찾으면 바로 이동. 더 발전없으면 끝

def run(self,p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i=0
    while i<self._limitStuck:
        successor = p.randomMutant(current) # 랜덤 이웃 생성
        valueS = p.evaluate(successor)  # 이웃 평가
        if valueS < valueC:     # 좋은 이웃이면 바로 이동
            current = successor
            valueC = valueS
            i = 0   # update한 current 바탕으로 다시 새로 돌자.
        else:
            i += 1
    
    p.storeResult(current, valueC)

## SteepestAscent(HillClimbing) : 기울기 가파른 정도에따라 따라감

def run(self,p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)  # 이웃들 소환
        successor, valueS = self.bestOf(neighbors,p)   
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current,valueC)

def bestOf(self,neighbors,p):
    best = neighbors[0]
    bestValue = p.evaluate(best)

    for neighbor in neighbors[1:]:  # 다돌면서 젤 best인 놈 찾기기
        valueN = p.evaluate(neighbor)
        if (valueN < bestValue):
            bestValue = valueN
            best= neighbor
    return best, bestValue

## GradientDescent(HillClimbing) : 연속그래프에서,  기울기따라 반대방향으로 계속 움직임

def run(self,p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        next = p.takeStep(current, valueC)
        valueN = p.evaluate(next)
        if valueN >= valueC:    # 다음 값이 현재보다 크거나 같으면,, 증가함수임..
            break
        else:
            current = next
            valueC = valueN
    p.storeResult(current,valueC)


## Stochastic(HillClimbing) 샘플기반 기울기방향으로 이동동

def run(self,p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i=0
    while i<self._limitStuck:
        neighbors = p.mutants(current)  # 이웃 생성
        next,valueS = self.stochasticBest(neighbors,p)  # 확률적으로 하나의 이웃을 선택
        if valueS < valueC: # 선택해가 더 나으면 이동
            current=next
            valueC = valueS
            i=0
        else:   # 아니면 탐색
            i+=1
    p.storeResult(current,valueC)

def stochasticBest(self, neighbors,p):
    valuesMin = [p.evaluate(indiv) for indiv in neighbors]  # 각해를 평가하여 list로 min에 저장한다.
    large = max(valuesMin)+1    # 젤 큰놈을 찾아+1해준다
    valuesMax = [large-val for val in valuesMin] # 작은값일수록 좋으니까, 큰값으로 변환해준다.

    # 확률계산을 위한 합
    total = sum(valuesMax)
    randValue = random.uniform(0,total)
    s = valuesMax[0]    # 누적 확률 저장

    for i in range(len(valuesMax)):
        if randValue <= s:  # 난수가 누적확률s보다 작거나 같으면 해당 해 선택택
            break
        else:   # randValue > s
            s+=valuesMax[i+1]
    
    nextSolution=neighbors[i]
    nextValue=valuesMin[i]
    return nextSolution, nextValue


## SimulatedAnnealing(MetaHeuristic)
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

def tSchedule(t):
    return t * (1-(1/10**4))    # t*(9999/10000)
