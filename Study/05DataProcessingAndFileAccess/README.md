# 05 Data Processing And File Access

## txt files
- `strVar = infile.readline()` : �����Ҷ����� pointer��ġ�� �����ٷ� �̵�
    - �������� ""��ȯ
    ![alt text](image.png)

- `outfile = open(filename,'w')` : ���� ������ ���� �� ����
- `outfile.writelines(list1)` : list1�� \n�� ������ �������ϴ� ��ü���� list
    -  (writeline �̵��� ����!!!!!!!!!!!!!!)
- `outfile.write(strVar)` : ���ڿ��ϳ� �Է�. �� �� �ǹ�X
    - (���� �Է��ϰ������ \n�־ �˾Ƽ� �Է��ϼ�)


```py
import os.path  # ���� ����, �̸� ����, ���� ���翩�� Ȯ���� ���� ���

if os.path.isfile("ABC.txt"):
    print("file already exist.")
else:
    infile = open("ABC.txt",'w')
    infile.write("a\nb\nc\n")
    infile.close()
```

- `os.remove(filename)` : ���� ���� (����������X)
- `os.rename(oldfilename,newfilename)` : ���ϸ� ���� (����������X)
- `os.path.isfile(filename)` : ���� ���� ���� Ȯ��

## csv files
- CSV(��ǥ�� ���е� ��) ����
- �� ���ο� ���� ������ �׸��� �������

## ���̳ʸ����Ͽ� dictionary �����ϱ�
- `pickle` ��� import �ؾ���
    ```py
    import pickle

    outfile = open(filename,'wb')
    pickle.dump(dicname,outfile)
    outfile.close()

    infile = open(filename,'rb')
    dicname = pickle.load(infile)
    infile.close()
    ```
    - ���̳ʸ����Ͽ� ���� Ȯ���ڴ� `".dat"`�̴�.