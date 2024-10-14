# 대통령도하고 부통령도한 사람 찾기
def main():
    fileName = "./file/VPres.txt"
    list1 = createListFromFile(fileName)
    createNewFile(list1,"./file/USPres.txt","./file/Both.txt")
def createListFromFile(fileName):
    infile = open(fileName, 'r')
    desiredList = [line.rstrip() for line in infile]
    
    infile.close()

    return desiredList

def createNewFile(listname, oldFilename, newFilename):
    infile = open(oldFilename,'r')
    outfile = open(newFilename,'w')

    for person in infile:
        if person.rstrip() in listname:
            outfile.write(person)

    infile.close()
    outfile.close()



main()