class Quizzes: 
    def __init__(self, listOfGrades): # 생성자
        self._listOfGrade = listOfGrades    # _listOfGrade 초기화
        self._average = 0   # _average 초기화

    def average(self): # 6개 점수중 젤 낮은걸 버리고남은 5개의 평균 점수를 _average에 저장
        self._average = (sum(self._listOfGrade)-min(self._listOfGrade))/5


    def __str__(self): # print할 값 return 
        return ("Quiz average: {}".format(self._average) )
 
def main(): 
    listOfGrades = []   # 빈 리스트 만들기

    for i in range(6):  # 6번입력 받아 list에 append하기
        listOfGrades.append(int(input("Enter grade on quiz {}: ".format(i+1))))

    q = Quizzes(listOfGrades)  # 객체 생성
    q.average() # average 계산하기
    print(q)   # Quiz average: 9.4 출력
 
main()