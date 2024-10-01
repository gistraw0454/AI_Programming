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