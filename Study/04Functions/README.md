# 04. Functions
```py
def functionName(par1, par2, par3 = val3 , par4 = val4):
    #code
    return returnValue
```

- `return` == `return None` == ` `
- Ű����� func(c=10,a=3) �̷������� ȣ���ϸ� �������ٴ� ������ �°� ��

## Scope of variable

### Local variable
- �Լ� ���ο��� �������. �Լ����ο����� �ν� ����. 
- �Լ� ȣ��ɶ����� ���� ��������� �����
### Global variable
- �Լ� �ۿ��� �������. ���α׷� ��� ������ �ν� ����.
- `global ������`�� ���� ������ �ٲ�� ������������ �ٲ��.
    - �̸��� ���Ͻ� ������ �켱���� (�� �ֱٿ� ������� ��)
    ```py
    x = 50

    def main():
        func()
        print(x)
    
    def func():
        global x    # ����������� ǥ�ø� ������� !

        print(x)
        x=2
        print(x)    # ���������� �ٲ�
    ```

### Named constant 
- ���α׷����� ���������Ǵ� Ư�� ���
- �� ���� `INTSERT_RATE = 0.04` �̷������� �빮�ڿ� `_`�� �������

## Library Modules
- Ȯ���ڰ� .py�� ����
    - import ��, ����Ҽ��ִ� �Լ��� �������� �������
- IDLE�� text editor ������ ������� �� �ִ�. 

```py
import ����

����.�Լ���   #����� �Լ�ȣ��
����.������   #����� ����ȣ��
```

### ��� import ���
1. Ư���Լ��� import 
    - `from random import randint, choice`
2. ����Լ� import
    - ����
3. interference���� ��ü ��� import
    - `����.`��� ȣ���ϸ��

- `as`�� ��Ī�� ����
    - `import numpy as np`
    - import �������� ���ص� �Ǳ���

![alt text](image.png)

## List Comprehension

- `list2 = [f(x) for x in list1]`
```py
list1 = ['2','5','8']
[int(x) for x in list1] # [2,5,8]

[g(x) for x in list1 if int(x) %2 == 1] # g(x) for x in list ���� ��, if�� ������ ����
```

## Lambda Expression
- `lambda par1, par2,... : expression`
```py
names = ["aaa ccc","bbb bbb", "ccc aaa"]
names.sort(key=lambda name: name.split()[-1])
nameString = ", ".join(names)
print(nameString)   # ccc aaa, bbb bbb, aaa ccc
```