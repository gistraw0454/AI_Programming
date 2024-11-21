class Student:
    def __init__(self,name="",mid =0,final=0):
        self._name = name
        self._mid = mid
        self._final = final
    
    def setName(self, name):
        self._name = name
    
    def setMid(self, mid):
        self._mid = mid
    
    def setFinal(self,final):
        self._final = final
    
    def getName(self):
        return self._name
    
    def __str__(self):
        return self._name + "\t" +self.calcSemGrade()  # 서브클래스에서 호출됨
    
class LGstudent(Student):   # subclass of Student
    def calcSemGrade(self):
        average = round((self._mid+self._final)/2)
        if average >=90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        else:
            return "F"

class PEstudent(Student):
    def calcSemGrade(self):
        average = round((self._mid + self._final)/2)
        if average>=60:
            return "Pass"
        else:
            return "Fail"
        