import matplotlib.pyplot as plt

def makeList(file_name):
    valueList = []
    with open(file_name, 'r') as file:  # ������ �б���� ����
        for line in file:   # ���� ���پ� �����鼭 
            valueList.append( float(line.strip()))  # �������� �� float ó���Ͽ� ����Ʈ�� ����
    return valueList

def plot_values(fileName1, fileName2, label1, label2):
    values1 = makeList(fileName1)
    values2 = makeList(fileName2)

    numeval1 = range(1, len(values1) + 1)   # ���� ���� (1~ ����Ʈ���̸�ŭ)
    numeval2 = range(1, len(values2) + 1)   # ���� ����

    plt.plot(numeval1, values1, label=label1, color='blue', linewidth=1.5)
    plt.plot(numeval2, values2, label=label2, color='orange', linewidth=1.5)
    
    # �� �̸� ���̱�
    plt.xlabel("Number of Evaluations")
    plt.ylabel("Tour Cost")
    plt.title("Search Performance (TSP-100)")

    
    plt.legend(loc='upper right', fontsize=5) # ���������� ����

    # �׷��� ����ϱ�
    plt.show()  # �����ֱ�


# Plot the values
plot_values("first.txt", "anneal.txt", "First-Choice Hill Climbing", "Simulated Annealing")
