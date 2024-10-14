def main():
    continent = input("input: ").title()    # 첫글자만 대문자로 변환
    if continent != "Antarctica":
        infile = open("./file/UN.txt",'r')
        for line in infile:
            data = line.split(',')
            if data[1] == continent:
                print(data[0])
    else:
        print("nothing.")


main()