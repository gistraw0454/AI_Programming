import Inheritance

class PFstudent(Student):
    def __init__(self, name="",mid=0,final=0,fullTime=True):
        super().__init__(name,mid,final)     # �̰� ���� ȣ���������
        self._fullTime = fullTime   # ���� ���ϴ� instance �߰�

    def setFullTime(self,fullTime):
        self._fullTime = fullTime
    
    def getFullTime(self):
        return self._fullTime
    
    def calcSemGrade(self):
        average = round((self._mid+self._final)/2)
        if average >=60:
            return "Pass"
        else:
            return "Fail"
    
    def __str__(self):
        if self._fullTime:
            status = "Full_time student"
        else:
            status = "part_time student"
        return (self._name + "\t" + self.calcSemGrade() + "\t" + status)