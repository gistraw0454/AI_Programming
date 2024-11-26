import matplotlib.pyplot as plt

def makeList(file_name):
    valueList = []
    with open(file_name, 'r') as file:  # 파일을 읽기모드로 열기
        for line in file:   # 파일 한줄씩 읽으면서 
            valueList.append( float(line.strip()))  # 공백제거 및 float 처리하여 리스트에 저장
    return valueList

def plot_values(fileName1, fileName2, label1, label2):
    values1 = makeList(fileName1)
    values2 = makeList(fileName2)

    numeval1 = range(1, len(values1) + 1)   # 범위 지정 (1~ 리스트길이만큼)
    numeval2 = range(1, len(values2) + 1)   # 범위 지정

    plt.plot(numeval1, values1, label=label1, color='blue', linewidth=1.5)
    plt.plot(numeval2, values2, label=label2, color='orange', linewidth=1.5)
    
    # 라벨 이름 붙이기
    plt.xlabel("Number of Evaluations")
    plt.ylabel("Tour Cost")
    plt.title("Search Performance (TSP-100)")

    
    plt.legend(loc='upper right', fontsize=5) # 오른쪽위로 설정

    # 그래프 출력하기
    plt.show()  # 보여주기


# Plot the values
plot_values("first.txt", "anneal.txt", "First-Choice Hill Climbing", "Simulated Annealing")
