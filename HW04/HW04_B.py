import math

class Fraction(): 
    def __init__(self, numerator=0, denominator=1):  # 생성자 _numerator, _denominator 초기화
        self._numerator = numerator
        self._denominator = denominator

    def getNumerator(self):  
        return self._numerator # _numerator return
    
    def setNumerator(self, value):  
        self._numerator = value    # _numerator 값 수정
      
    def getDenominator(self):  
        return self._denominator    # _denominator return
    
    def setDenominator(self, value):  
        self._denominator = value   # _denominator 값 수정

    def print(self):  
        print("\nThe fraction is {}/{}".format(self._numerator, self._denominator))   # The fraction is 930/2170
 
class IrreducibleFraction(Fraction):  
    def __init__(self, numerator=0, denominator=1):  
        super().__init__(numerator, denominator)  # super()로 먼저, 부모 생성자 호출 -> 이후 원하는 값 추가
        gcd = self._GCD(numerator, denominator)  # gcd계산하기
        self._numerator //= gcd         # 나눠서 정수 결과 추출
        self._denominator //= gcd 

    def _GCD(self, m, n):  
        return math.gcd(m, n)  # math import해서 gcd 계산 후 return 

    def print(self):  
        print("The reduced fraction is {}/{}".format(self._numerator, self._denominator))   # The reduced fraction is 3/7
 
def main():  
    numerator = eval(input('Enter the Numerator: '))  
    denominator = eval(input('Enter the Denominator: '))  
    fraction = Fraction(numerator, denominator) # fraction 객체 (부모) 생성
    fraction.print()  

    reduced_fraction = IrreducibleFraction(numerator, denominator) # 자식 객체 생성
    reduced_fraction.print()  

main()
