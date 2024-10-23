def main():
    vicePresList = createListFromFile("VPres.txt")
    createNewFile(vicePresList,"UsPres.txt","Both.txt")
    
def createListFromFile(filename):
    infile = open(filename,'r')
    desiredList = [line.rstrip() for line in infile]
    infile.close()
    return desiredList

def createNewFile(listname, oldfilename, newfilename):
    infile = open(oldfilename,'r')
    outfile = open(newfilename,'w')
    for person in infile:
        if person.rstrip() in listname:
            outfile.write(person)
    infile.close()
    outfile.close()