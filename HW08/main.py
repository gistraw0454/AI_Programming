# Main 함수의 역할
# 1. 어떤 유형(TSP, Numeric)의 어떤 문제(tsp30.txt, 
# Ackley.txt, …)를 풀 것인지 입력 받기
# 2. 어떤 알고리즘으로 풀지 입력 받기
# 3. Problem/Optimizer Class를 이용해서 문제풀기
# 4. 결과 출력하기

from problem import *
from optimizer import *

def main():
    p, pType = selectProblem()  # p
    alg = selectAlgorithm(pType)

    # if issubclass(type(alg),HillClimbing):
    #     alg.randomRestart(p)
    # else:
    #     alg.run(p)

    # 탐색 알고리즘 호출
    alg.randomRestart(p)
    # 문제 해결
    p.describe()
    # 알고리즘 세팅
    alg.displaySetting()
    # 결과 출력
    p.report()
    
def selectProblem():
    print("Select the problem type:")
    print(" 1. Numerical Optimization")
    print(" 2. TSP")
    # 1 (Numeric) 또는 2 (TSP)를 입력 받아서 대응되는 Problem Class를 초기화해서 반환하기
    
    pType = int (input("Enter the number: "))
    if pType == 1:  
        p = Numeric()   # 입력값 1,0 에 따라서 빈 문제 객체 만들기
    elif pType == 2:
        p = Tsp()
    p.setVariables()    # 특정 문제 객체 변수설정하기
    return p, pType


def selectAlgorithm(pType):
    print()
    print("Select the search algorithm:")
    print(" 1. Steepest-Ascent")
    print(" 2. First-Choice")
    print(" 3. Gradient Descent")
    print(" 4. Stocahstic")
    print(" 5. SimulatedAnnealing")

    while True:
        aType = int (input("Enter the number: "))
        if not invalid(pType, aType):
            break
    optimizers = {1:'SteepestAscent()',
                  2: 'FirstChoice()',
                  3: 'GradientDescent()',
                   4: 'Stochastic()',
                    5: 'SimulatedAnnealing()'}
    alg = eval (optimizers[aType])
    alg.setVariables(pType)
    return alg

def invalid(pType, aType):
    if pType==2 and aType==3:
        print("You cannot choose Gradient Descent")
        print(" unless your want a function optimization.")
        return True
    else:
        return False


    # pType == 2 (TSP)일 경우, Gradient Descent를 입력 받으면 사용자로부터 재입력 받도록 구현
    # pType과 aType이 올바르게 설정 됐는지 확인하기 위한 invalid(pType, aType) 함수 추가 구현
    

main()