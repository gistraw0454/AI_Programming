def main():
    file = "./FirstPresidents.txt"
    displayWithForLoop(file)
    print()
    deisplayWithListComprehension(file)
    print()
    displayWithReadline(file)

def displayWithForLoop(file):
    infile = open(file,'r')
    for line in infile:
        print(line.rstrip())
    infile.close()

def deisplayWithListComprehension(file):
    infile = open(file,'r')
    listPres = [line.rstrip() for line in infile]
    infile.close()
    print(listPres)

def displayWithReadline(file):
    infile = open(file,'r')
    line = infile.readline()
    while line != "":
        print(line.rstrip())
        line = infile.readline()
    infile.close()
    
main()