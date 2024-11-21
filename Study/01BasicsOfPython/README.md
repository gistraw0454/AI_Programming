# 01. Basics of Python

> str.upper() �̷��� �޼ҵ�, len(str) �̷��� �Լ������.

|Expression|Explaination|
|---|---|
|`type(��)`| str, float, tuple �� ���� type�� �˷��� |
|`abs(��)`| ���� |
|`int(��)`|�Ҽ������� ����|
|`round(��,[��°�ڸ�����?])`|�ݿø�|

```py
n=5 # 5�� �����ϴ� �޸𸮺κ��� ���� n�� �����Ѵ�.
n=7 # ������ 5�� garbage collection �� �����ϰԵȴ�.
```

## String
- immutable �ѹ� ���ϸ� �ٲ� �� ����.

|Expression|Explaination|
|---|---|
|`eval(str����)`|ǥ������ �����Ǵ� FP�� ��|
|`exec(str����)`|<ins>python expression</ins>�� ������ ���ڿ� ����|
|`str(����)`|���ڿ��� �ٲ�|
|`ord(����)`|�ƽ�Ű ���ڷ� �ٲ�|
|`chr(����)`|�ƽ�Ű ���ڷ� �ٲ���|
            
![alt text](image.png)

```py
print('Python'[2:4])    # 2���� 4-1���� ���
print('Python'.find('th'))  # 2 # ������ -1 ���
print('Python'.rfind('l'))  # rightmost l�� ã�´�.
```

## Optional print Arguments
```py
print("hello","world",sep="*")  # hello*wolrd\n
print("hello",end="")   # hello

print('''{} was {}.
kk'''.format('name',20))

# < ���� ���� ^ ��� ���� > ������ ����
# default : ���ڴ� ����, ���ڿ��� ������ ����
print("{0:^5}{1:<20}{2:>3}".format(1,"name anme",832))

print('{0:_^11}'.format('hello'))   # ___hello___

print('${0:,.2f}'.format(11163.75423))  # $11,163.75

```

![alt text](image-1.png)
