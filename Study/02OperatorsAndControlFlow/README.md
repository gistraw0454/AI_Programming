# 02. Operators and Control flow

```py
print(15/3) # 5.0 
print(15//3)    #  ���� ������ 5 
print(-25.5%2.25)   #1.5
print(~5)   # -6    ~x+1 = -x
```

|notation|meaning|
|--|--|
|==,!=,<,>,<=,>=||
|in|substring of|
|not in|not a substring of|
|is||
|is not||
|lambda||
|`x[index]`,`x[index:index]`,`x(arguments)`,`x.attribute`|subscription, slicing, call, attribute, reference|
|`(a,b,..)`,`[a,b,..]`,`{key:value,..}`,`{a,b,..}`|binding or tuple, list, dictionary, set|

|method|returns true when|
|--|--|
|str1.isdigit()|char�� ����|
|str1.isalpha()|char�� ���ĺ�|
|str1.isalnum()|char�� ���ڶǴ� ���ĺ�|
|str1.islower()|����ִ� ��� ���ĺ��� �ҹ���|
|str1.isupper()|����ִ� ��� ���ĺ��� �빮��|
|str1.isspace()|whitespace char����|

## loop
- `for var in sequence:`
    - sequence: numbers, string, list, tuple, file object
    - range(m,n,s)  : m���� n-1���� s ��������.. (s default�� 1)

```py
infile = open('filename.txt','r')
for line in infile:
    #code
infile.close()
```

- whitespace : spaces, new line (\n), tabs (\t) ���� rstrip method�� ���Ű���
