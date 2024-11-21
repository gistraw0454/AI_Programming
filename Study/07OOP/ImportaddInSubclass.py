import addInSubclass

def main():
    name = input("name: ")
    mid = float(input("mid: "))
    final = float(input("final: "))

    category = input("LG? PF?")

    if category.upper == "LG":
        st = addInSubclass.LGstudent(name,mid,final)
    else:
        fullTime = True
        st = addInSubclass.PFstudent(name,mid,final,fullTime)

    print(st)

main()