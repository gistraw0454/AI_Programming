from numeric import *

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomMutant(current, p): ### TODO
    nop, domain = p # p가 (a,b) 형태를 가지므로 두값을 모두 받아와 domain만 사용
    varNames, low, up = domain # domain값 (,,)로 따로 저장
    i = random.randint(0, len(current) - 1) # current 기준으로 랜덤한 int 값을 뽑아 index를 만들어 준다.
    randomValue = random.random()   
    if (randomValue >0.5):  # 50% 확률로 랜덤하게 + or - 방향을 결정해준다. 
        d = DELTA
    else:
     d = -DELTA 
    mutant = current[:] # 완전히 복사한 리스트를 만들어 준다.
    
    mutant[i] = max(min(mutant[i] + d, up[i]), low[i])  # up, low 범위내에서 벗어나지않게 min, max를 걸어주고 선택한 방향으로 이동시켜준다.
    return mutate(current, i, d, p) # 수정한 값을 리턴한다.


def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()
