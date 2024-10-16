import LGstudents

def main():
    listStudent = []
    carryOn = 'Y'
    while carryOn == 'Y':
        st = LGstudents.LGstudent() # 객체 생성
        name = input("name: ")
        mid = float(input("mid: "))
        final = float(input("final: "))

        st = LGstudents.LGstudent(name,mid,final)

        listStudent.append(st)
        carryOn = input("Y/N? ")
        carryOn = carryOn.upper()
    for i in listStudent:
        print(i)

main()