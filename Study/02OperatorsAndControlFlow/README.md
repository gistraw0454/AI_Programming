# 02. Operators and Control flow

```py
print(15/3) # 5.0 
print(15//3)    #  정수 나누기 5 
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
|str1.isdigit()|char이 숫자|
|str1.isalpha()|char가 알파벳|
|str1.isalnum()|char가 숫자또는 알파벳|
|str1.islower()|들어있는 모든 알파벳이 소문자|
|str1.isupper()|들어있는 모든 알파벳이 대문자|
|str1.isspace()|whitespace char포함|

## loop
- `for var in sequence:`
    - sequence: numbers, string, list, tuple, file object
    - range(m,n,s)  : m부터 n-1까지 s 간격으로.. (s default는 1)

```py
infile = open('filename.txt','r')
for line in infile:
    #code
infile.close()
```

- whitespace : spaces, new line (\n), tabs (\t) 들은 rstrip method로 제거가능
