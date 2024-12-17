def takeStep(self,x,valueC):
        grad = self.gradient(x,valueC) 
        xCopy = x[:]
        for i in range(len(xCopy)):
            xCopy -= self._alpha*grad[i]  
        
        if self.isLegal(xCopy):
            return xCopy
        else:
            return x   
    
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

## FirstChoice(HillClimbing)
def run(self, p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i = 0
    while i < self._limitStuck:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    p.storeResult(current, valueC)

## SteepestAscent(HillClimbing)
def run(self, p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = self.bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current, valueC)

def bestOf(self, neighbors, p):
    best = neighbors[0]
    bestValue = p.evaluate(best)
    for neighbor in neighbors[1:]:
        valueN = p.evaluate(neighbor)
        if valueN < bestValue:
            bestValue = valueN
            best = neighbor
    return best, bestValue

## GradientDescent(HillClimbing)
def run(self, p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    while True:
        next = p.takeStep(current, valueC)
        valueN = p.evaluate(next)
        if valueN >= valueC:
            break
        else:
            current = next
            valueC = valueN
    p.storeResult(current, valueC)

## Stochastic(HillClimbing)
def run(self, p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    i = 0
    while i < self._limitStuck:
        neighbors = p.mutants(current)
        next, valueS = self.stochasticBest(neighbors, p)
        if valueS < valueC:
            current = next
            valueC = valueS
            i = 0
        else:
            i += 1
    p.storeResult(current, valueC)

def stochasticBest(self, neighbors, p):
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
    nextSolution = neighbors[i]
    nextValue = valuesMin[i]
    return nextSolution, nextValue

## SimulatedAnnealing(MetaHeuristic)
def run(self, p):
    current = p.randomInit()
    valueC = p.evaluate(current)
    best, valueBest = current, valueC
    whenBestFound = 1
    i = 1
    t = self.initTemp(p)
    while True:
        t = self.tSchedule(t)
        if t == 0 or i == self._limitEval:
            break
        next = p.randomMutant(current)
        valueN = p.evaluate(next)
        dE = valueN - valueC
        if dE < 0:
            current = next
            valueC = valueN
        else:
            if random.uniform(0, 1) < math.exp(-dE / t):
                current = next
                valueC = valueN
        if valueC < valueBest:
            best, valueBest = current, valueC
            whenBestFound = i
    self._whenBestFound = whenBestFound
    p.storeResult(best, valueBest)

def initTemp(self, p):
    diffs = []
    for i in range(self._numSample):
        c0 = p.randomInit()
        v0 = p.evaluate(c0)
        c1 = p.randomMutant(c0)
        v1 = p.evaluate(c1)
        diffs.append(abs(v1 - v0))
    dE = sum(diffs) / self._numSample
    t = dE / math.log(2)
    return t

def tSchedule(t):
    return t * (1 - (1 / 10**4))
