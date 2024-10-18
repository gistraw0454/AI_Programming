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
        while(True):
            choice =  (input("{}, enter your choice: ".format(self.getName())))
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            else:
                print(f"invalid choice {choice}\n")
 
class Computer(Contestant):  
    def makeChoice(self):  
        elements = ['rock','scissors','paper']
        result = random.choice(elements)
        print("{} chooses {}".format(self.getName(),result))
        return result
 
def playGame(h, c):  
    choiceH = h.makeChoice()  
    choiceC = c.makeChoice()  
    if choiceH == choiceC:  
        pass  
    elif judge(choiceH, choiceC):  
        h.setScore(h.getScore() + 1)  
    else:  
        c.setScore(c.getScore() + 1)  
 
def judge(choiceH, choiceC):  
    if ((choiceH == 'rock' and choiceC == 'scissors') or 
        (choiceH == 'paper' and choiceC == 'rock') or 
        (choiceH == 'scissors' and choiceC == 'paper')):  
        return True  
    else:  
        return False  
 
def main():  
    human = Human(input("Enter name of human: "))
    computer = Computer(input("Enter name of computer: "))
    print()

    for i in range(3):
        playGame(human,computer)
        print(f"{human.getName()}: {human.getScore()}, {computer.getName()}: {computer.getScore()}")
        print()

    if (human.getScore()>computer.getScore()):
        print(f"{human.getName()} WIN")
    elif (human.getScore()<computer.getScore()):
        print(f"{human.getName()} LOSE")
    else:
        print("TIE")
main()