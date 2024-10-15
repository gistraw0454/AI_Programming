# 07 OOP (object-oriented programming)

## Classes and Objects
- class : 객체가 생성되는 templete
    - str, int, float, list, tuple, dictionary 는 built-in python classes
    - class의 각 instance(객체)에는 고유 값이 있다.
    ```py
    class className:
        #method
    ```
    - 메서드는 첫번째 매개변수로 self를 갖는다.
        - 객체가 생성되는 각 메서드의 self 매개변수는 객체를 참조
    - `__init__` method (생성자) 는 객체가 생성될 때 자동으로 호출되어 인스턴수 변수(클래스의 속성)에 값을 할당한다.

    - `__str__` method : 객체의 상태(instance 변수값)을 문자열로 표현하는 사용자 지정 방식 제공

    - 객체 생성 방법?
        ```py
        objectName = ClassName(arg1,arg2,...)
        
        objectName = modulName.ClassName(arg1,arg2,...)
        ```


> 객체 변수 명은 `_`로 시작하므로 클래스 정의 외부에서 직접 엑세스할 수 없다. 
    - 객체 지향 프로그램이은 클래스 사용자에게 메서드 구현을 숨긴다.