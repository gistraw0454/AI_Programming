# 리스트 입력 받기
list1 = list(map(int, input("Enter measurements as a list: ")[1:-1].split(", ")))
    # list1 = [int(i) for i in list1]

# 리스트 sort하기 
list1.sort()

# 리스트 길이 구하기
listLen = len(list1)

# 리스트 홀짝 구분하여 median 계산

# odd
if listLen % 2 == 1:
    median = list1[listLen//2]

# even
else:
    median = (float)(list1[listLen//2-1] + list1[listLen//2])/2

# Median 출력
print("Median: {:.1f}".format(median))

# list 인덱스값은 int여야하므로 listLen/2 이 아니라, listLen//2로 계산할 것.