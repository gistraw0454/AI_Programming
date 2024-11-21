from problem import Tsp

LIMIT_STUCK = 100 


def main():
    p = Tsp()   # 객체 생성
    p.setVariables()    # 파일 읽어와서 초기화하기
    # Call the search algorithm
    firstChoice(p)
    # Show the problem and algorithm settings
    p.describe()        # 출력 
    displaySetting()   
    
    # Report results
    p.report() 
    

def firstChoice(p): # first-choice 함수 정의
    current = p.randomInit()    # 랜덤한 current 결정
    valueC = p.evaluate(current)    # 현재의 evaluation 계산
    
    i = 0
    while i < LIMIT_STUCK:  # limit 만큼 돌면서 새 solution을 찾을 때까지 계속 돌아준다.
        successor = p.randomMutant(current) # randMutant로 랜덤하게 변형하여 solution을 만든다.
        valueS = p.evaluate(successor)  # 그 솔루션의 evalution을 계산한다.
        if valueS < valueC: # new solution이 더 좋으면 바꿔준다. <- 반복
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    p.storeResult(current, valueC)  # 최적의 solution을 저장


def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")

main()
