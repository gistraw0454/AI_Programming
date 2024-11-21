import Inheritance

def main():
    listOfStudents = obtainListOfStudents()
    displayResults(listOfStudents)

def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'

    while carryOn == 'Y':
        name = input("name: ")
        mid = float(input("mid: "))
        final = float (input("final: "))

        category = input("LG? PF?")
        if category.upper() == 'LG':
            st = Inheritance.LGstudent(name,mid,final)
        else:
            st = Inheritance.PEstudent(name,mid,final)
        
        listOfStudents.append(st)
        carryOn = input("continue? Y/N")
        carryOn = carryOn.upper()
    
    return listOfStudents

def displayResults(listOfStudents):
    listOfStudents.sort(key=lambda x: x.getName())
    for i in listOfStudents:
        print(i)

main()