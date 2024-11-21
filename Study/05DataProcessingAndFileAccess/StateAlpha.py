def main():
    statelist = createListFromFile("./file/States.txt")
    createSortedFile(statelist, "./file/StatesAlpha.txt")

def createListFromFile(filename):
    infile = open(filename, 'r')
    filelist = [line.rstrip() for line in infile]
    infile.close()
    return filelist

def createSortedFile(listname, filename):
    for i in range(len(listname)):
        listname[i] = listname[i]+"\n"
    outfile = open(filename,'w')
    outfile.writelines(listname)
    outfile.close()


main()