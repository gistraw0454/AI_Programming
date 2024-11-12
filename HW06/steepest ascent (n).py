from problem import Numeric

def main():
    
    p = Numeric()   
    p.setVariables()    # 객체 생성 및 파일 읽어 초기화하기
    
    steepestAscent(p)   # steepsetAscent 함수 호출
    
    p.describe()    # 알고리즘 셋팅 출력하기
    displaySetting(p)
    
    p.report()  # 결과 출력

def steepestAscent(p):  # steepestAscent 함수 정의
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors,p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current,valueC)


def bestOf(neighbors, p): ### TODO
    best = neighbors[0]
    bestValue = p.evaluate(best)
    
    for neighbor in neighbors[1:]:
        value = p.evaluate(neighbor)
        if value < bestValue:
            best = neighbor
            bestValue = value
    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()
