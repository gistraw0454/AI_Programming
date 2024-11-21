def main():
    name = input("name: ")
    mid = float(input("mid exam: "))
    final = float(input("final exam: "))

    st = LGstudent(name, mid, final)
    print(st)

class LGstudent:
    def __init__(self,name="",mid=0,final=0):
        self._name = name
        self._mid = mid
        self._final = final

    def setName(self,name):
        self._name = name
    
    def setMid(self,mid):
        self._mid = mid
    
    def setFinal(self,final):
        self._final = final
    
    def calcSemGrade(self):
        grade = ( self._mid + self._final )/2
        grade = round(grade)

        if grade >=90:
            return "A"
        elif grade >=80:
            return "B"
        elif grade >=70:
            return "C"
        else:
            return "F"
        
    def __str__(self):  # 객체 생성시 수행되는 부분
        return self._name+"\t"+self.calcSemGrade()


main()