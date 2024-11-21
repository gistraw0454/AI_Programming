# 딕셔너리 연산자를 써라. 
# create dictionary from Units.txt to convert units.
def populateDictionary():
    File = open("./Units.txt",'r')  # r 읽기모드로 열기
    newDic = {} # 빈 딕셔너리 만들기
    for line in File:   # File 한줄씩 읽으면서 line에 저장
        unit,length = line.strip().split(",")   # 양쪽 공백 제거 후 "," 기준으로 두개로 나눠 unit과 length에 각각 저장
        newDic[unit] = float(length)    # 딕셔너리 원소 추가 unit은 key로 length는 float으로 바꿔 value로 추가
    File.close()    # 닫기
    return newDic
        
# Input units and length from the terminal.
def getInput(): 
    orig = input("Unit to convert from: ")
    dest = input("Unit to convert to: ")
    length = int(input("Enter length in yard: "))   # 길이만 int형으로 바꿔서 입력 받는다.
    return orig,dest,length # 순서대로 ret
 
def main():
    feet = populateDictionary() 
    orig, dest, length = getInput() 
    answer = length * feet[orig] / feet[dest] 
    print("Length in {0}: {1:,.4f}".format(dest, answer)) 
 
main()