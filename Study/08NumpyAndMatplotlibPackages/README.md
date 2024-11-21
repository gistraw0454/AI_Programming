# Numpy

```python
#%% Array
import numpy as np

a= np.array([1,2,3])
b= np.array([[1,2],[3,4]])    # 2d
c= np.array([1,2,3,4,5],ndmin=2)    # [[1 2 3 4 5]]
d= np.array([1,2,3],dtype=float)    # [1. 2. 3.]

#%% Array Creation arange는 arr. range만큼 가져온다 생각하면된다.
import numpy as np
a = np.arange(5)    # [0 1 2 3 4]
b = np.arange(3,9,2)    # [3 5 7]    
                        #c = .zeros(5) .ones(5)
c = np.eye(3)   # I 3
d = np.eye(3,4) # I 3x4
e = np.linspace(10,20,5)    # [10. 12.5 15. 17.5 20.] 10부터 20까지 5분할하기

#%% Changing Shape
import numpy as np

a = np.arange(6)
print(a)
b = a.reshape(3,2)
np.shape(b) # (3,2)
np.size(b)  # element 개수?
np.ndim(b)  # 몇차?
np.transpose(b) 

c = np.copy(b)  # 복사 
np.ravel(b) # 1d 로 바꾸기 []

# 행렬끼리 dot 연산과 inner연산도 가능 np.inner(a,b)

#%% Random
import numpy as np
b = np.random.rand(3,2) # 3x2 (0~1)값의 임의의 행렬 만들기
c = np.random.randint(3,9,size=(2,4))   # 3~8 int로 2x4만들기
print(b)
print(c)
```

# Matplotlib 

# Pandas

```python
#%% Series, Dataframe
import pandas as pd
ser = pd.Series(data=[1,2,3],index=['a','b','c'])
print(ser)
print(ser['a'])

d = {'col1':[1,2],'col2':[3,4]}
df = pd.DataFrame(data=d)
print(df['col1'])
print(df['col1'][0])
```

### CSV 읽고 쓰기**

```python
iris = pd.read_csv('경로')	# 읽기

iris.to_excel('파일명')	# to_csv('파일명') 쓰기
```

# 과제

```python
// 1~ 1000000 짝수들의 각 자릿수 합치기
totalSum = 0
for odd in range(1,1000000,2):
    
    numSum = 0
    for i in str(odd):
        numSum += int(i)
    totalSum += numSum

print("The sum of the digits of odd numbers\nFrom 1 to one million is {:,}.".format(totalSum))
```

```python3
# 10000~ 99999 사이의 A*4 == A 뒤집은값인 값 찾기
# reverse, join format 쓸 것

for i in range(10000,100000):
    # ['1','0','0','0','0']
    strNum = list(str(i))

    # ['1','0','0','0','0'] -> ['0','0','0','0','1']
    strNum.reverse()    # 뒤집고 None을 반환
    
    # ['0','0','0','0','1'] -> '00001' -> 1
    revNum = int("".join(strNum))
    
    if (revNum==4*i):
        print("Since 4 * {} is {},".format(i,i*4))
        print("The special number is {}.".format(i))
        break

```

```python3
# 알파벳 순서로 된 리스트를 가진 txt파일을 읽고 입력값이 있는지 없는지 파악 (읽을때 set형식으로 받기)
# set operation 쓰기, os.path.isfile 과 exit 함수를 써라 readsetfromfile에서.. 
import os.path 

# read set from Names.txt. If the file does not exist, exit
def readSetFromFile():        #implement functions 
    # 파일이 존재하면 파일을 읽기모드로 열고, set으로 저장하기
    if os.path.isfile("./Names.txt"):
        File = open("./Names.txt","r")
        nameSet = {line.strip() for line in File}  # 한줄읽고 \n제거하여 저장
    else:
        print("Name.txt does not exist.\nTerminate program.")
        exit()  # 파일 존재하지 않으면 종료
    return nameSet

# input the name from the terminal.
def inputName():    # 이름 입력받고 return 
    newName = input("Enter a first name to be included: ")
    return newName

# insert the name into set
def insertSet(mySet, name):
    # mySet과 name의 교집합이 있으면 "이미 있다" 출력, 없으면 "추가" 출력.
    if name in mySet:   # if mySet.intersection({name}):   
        print("{} is already in Names.txt".format(name))
    else:
        print("{} is added in Names.txt".format(name))
    mySet.add(name) # set은 중복이 안되므로 그냥 넣어도 될 듯.
    return mySet

# write set to Names.txt. 
def writeToFile(modifiedSet): 
    # 쓰기모드로 파일 열고 (덮어써야함) set을 정렬하여 하나씩 뽑아 txt에 저장
    File = open("./Names.txt","w") # set은 순서가 없기때문에 그냥 따로하는건 의미없음..
    for name in sorted(modifiedSet): # sorted(set)이 정렬된 list를 반환하기 때문에 list에서 뽑아 txt에 저장       
        File.write(name+'\n')
    File.close()

def main():  
    mySet = readSetFromFile() 
    name = inputName() 
    modifiedSet = insertSet(mySet, name) 
    writeToFile(modifiedSet) 
 
main()
```

```python3
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
```

-------------------------

### class (class 메소드부분만 채울줄 알면되긴함)

```python3
class Quizzes: 
    def __init__(self, listOfGrades): # 생성자
        self._listOfGrade = listOfGrades    # _listOfGrade 초기화
        self._average = 0   # _average 초기화

    def average(self): # 6개 점수중 젤 낮은걸 버리고남은 5개의 평균 점수를 _average에 저장
        self._average = (sum(self._listOfGrade)-min(self._listOfGrade))/5


    def __str__(self): # print할 값 return 
        return ("Quiz average: {}".format(self._average) )
 
def main(): 
    listOfGrades = []   # 빈 리스트 만들기

    for i in range(6):  # 6번입력 받아 list에 append하기
        listOfGrades.append(int(input("Enter grade on quiz {}: ".format(i+1))))

    q = Quizzes(listOfGrades)  # 객체 생성
    q.average() # average 계산하기
    print(q)   # Quiz average: 9.4 출력
 
main()
```

```python3
import math

class Fraction(): 
    def __init__(self, numerator=0, denominator=1):  # 생성자 _numerator, _denominator 초기화
        self._numerator = numerator
        self._denominator = denominator

    def getNumerator(self):  
        return self._numerator # _numerator return
    
    def setNumerator(self, value):  
        self._numerator = value    # _numerator 값 수정
      
    def getDenominator(self):  
        return self._denominator    # _denominator return
    
    def setDenominator(self, value):  
        self._denominator = value   # _denominator 값 수정

    def print(self):  
        print("\nThe fraction is {}/{}".format(self._numerator, self._denominator))   # The fraction is 930/2170
 
class IrreducibleFraction(Fraction):  
    def __init__(self, numerator=0, denominator=1):  
        super().__init__(numerator, denominator)  # super()로 먼저, 부모 생성자 호출 -> 이후 원하는 값 추가
        gcd = self._GCD(numerator, denominator)  # gcd계산하기
        self._numerator //= gcd         # 나눠서 정수 결과 추출
        self._denominator //= gcd 

    def _GCD(self, m, n):  
        return math.gcd(m, n)  # math import해서 gcd 계산 후 return 

    def print(self):  
        print("The reduced fraction is {}/{}".format(self._numerator, self._denominator))   # The reduced fraction is 3/7
 
def main():  
    numerator = eval(input('Enter the Numerator: '))  
    denominator = eval(input('Enter the Denominator: '))  
    fraction = Fraction(numerator, denominator) # fraction 객체 (부모) 생성
    fraction.print()  

    reduced_fraction = IrreducibleFraction(numerator, denominator) # 자식 객체 생성
    reduced_fraction.print()  

main()

```

```python3
import random  
 
class Contestant:  
    def __init__(self, name="", score=0):  # 생성자 _name, _score 초기화
        self._name = name
        self._score = score

    def getName(self):  # _name return
        return self._name
    
    def getScore(self):    # _score return
        return self._score
      
    def setScore(self,value):  # set _score
        self._score = value 
    
    def setName(self,name): # set _name
        self._name = name

class Human(Contestant): 
    def makeChoice(self):  
        while(True):    # rock, paper scissors중에 입력이없으면, invalid choice 출력 후, 무한 루프를 돈다.
            choice =  (input("{}, enter your choice: ".format(self.getName()))) # choice에 입력값을 저장해 옳은 값을 입력했는지 확인
            if choice in ['rock', 'paper', 'scissors']:
                return choice   # 옳은 값을 입력한 경우, 해당값을 return 
            else:
                print(f"invalid choice {choice}\n") # 잘못된 값 입력한 경우, 무한 루프
 
class Computer(Contestant):  
    def makeChoice(self):  
        elements = ['rock','scissors','paper']  # rock scissors paper중에 랜덤으로 하나의 요소를 뽑아 result에 저장
        result = random.choice(elements)
        print("{} chooses {}".format(self.getName(),result))   
        return result   # 해당 result값 return 
 
def playGame(h, c):  
    choiceH = h.makeChoice()   # 뽑은값을 각각 저장
    choiceC = c.makeChoice()  
    if choiceH == choiceC:      # 동일한 경우 pass
        pass  
    elif judge(choiceH, choiceC):   # 이겼으면 human score을 1증가
        h.setScore(h.getScore() + 1)    
    else:                               # 잔경우, computer score 1증가
        c.setScore(c.getScore() + 1)  
 
def judge(choiceH, choiceC):  
    if ((choiceH == 'rock' and choiceC == 'scissors') or 
        (choiceH == 'paper' and choiceC == 'rock') or 
        (choiceH == 'scissors' and choiceC == 'paper')):  
        return True  # 승패 확인
    else:  
        return False  
 
def main():  
    human = Human(input("Enter name of human: "))   # 사람과 컴퓨터이름 입력 받기
    computer = Computer(input("Enter name of computer: "))
    print()

    for i in range(3):  # 3번 진행
        playGame(human,computer)
        print(f"{human.getName()}: {human.getScore()}, {computer.getName()}: {computer.getScore()}")    # 게임한판할때마다 score 출력
        print()

    if (human.getScore()>computer.getScore()):  # human의 score값이 더 큰경우, 승리 
        print(f"{human.getName()} WIN")
    elif (human.getScore()<computer.getScore()):    # human의 score값이 더 작은 경우 패배
        print(f"{human.getName()} LOSE")
    else:
        print("TIE")    # 같으면 TIE
main()
```

