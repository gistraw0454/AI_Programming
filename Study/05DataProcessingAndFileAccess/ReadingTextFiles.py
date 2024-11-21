def main():
    file = "./file/FirstPresidents.txt"
    displayWithForLoop(file)
    print()
    displayWithListComprehension(file)
    print()
    displayWithReadline(file)

def displayWithForLoop(file):
    infile = open(file,'r')
    for line in infile:
        print(line.rstrip())    # rstrip로 \n제외하고 출력.
    infile.close()

def displayWithListComprehension(file):
    infile = open(file,'r')
    listPres = [line.rstrip() for line in infile]   # list로 반환
    infile.close()
    print(listPres)

def displayWithReadline(file):
    infile = open(file,'r')
    line = infile.readline()    # 한줄읽기 (커서 부분이 바뀜)
    while line != "":
        print(line.rstrip())
        line = infile.readline()
    infile.close()

main()
