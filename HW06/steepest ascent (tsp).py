from problem import Tsp

def main():
    # Create an instance of TSP
    p = Tsp()   
    p.setVariables()    # 객체 생성 및 파일 읽어 초기화하기
    
    steepestAscent(p)   # steepsetAscent 함수 호출
    
    p.describe()    # 알고리즘 셋팅 출력하기
    displaySetting()
    
    p.report()  # 결과 출력

def steepestAscent(p):
    current = p.randomInit()   # 'current' is a list of city ids  # 함수 호출 -> 메서드 호출 방식으로 변경
    valueC = p.evaluate(current)     # 함수 호출 -> 메서드 호출 방식으로 변경
    while True:
        neighbors = p.mutants(current)   # 함수 호출 -> 메서드 호출 방식으로 변경
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def bestOf(neighbors, p): ### TODO
    best = neighbors[0]
    bestValue = p.evaluate(best)    # 함수 호출 -> 메서드 호출 방식으로 변경
    
    for i in range(1, len(neighbors)):  # 모든 이웃을 돌면서 현재이웃의 평가값을 계산하고 최적의 값을 찾는다.
        newValue = p.evaluate(neighbors[i])  # 함수 호출 -> 메서드 호출 방식으로 변경 (평가값 계산)
        if newValue < bestValue:    # 현재 좋은 평가값 < 새 평가값 이면 갱신해주기 !
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue  # 최적의 값 리턴

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")


main()
