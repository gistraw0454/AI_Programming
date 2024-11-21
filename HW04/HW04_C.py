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