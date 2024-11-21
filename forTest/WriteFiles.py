def main():
    L = ["asndlnwlfnkw","saklfkasnklnasfkl","dklasdlasjkdljasklghalsf"]
    outfile = open("FirstPresidents2.txt","w")
    createWithWrite(L,outfile)
    outfile = open("FirstPresident3.txt",'w')
    createWithWritelines(L,outfile)


def createWithWrite(L,outfile):
    for i in range(len(L)):
        outfile.write(L[i]+"\n")
    outfile.close()

def createWithWritelines(L,outfile):
    for i in range(len(L)):
        L[i] = L[i] +'\n'
    outfile.writelines(L)
    outfile.close()

main()
