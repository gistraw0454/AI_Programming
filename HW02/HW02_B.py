# 10000~ 99999 사이의 A*4 == A 뒤집은값인 값 찾기
# reverse, join format 쓸 것

for i in range(10000,100000):
    # ['1','0','0','0','0']
    strNum = list(str(i))

    # ['1','0','0','0','0'] -> ['0','0','0','0','1']
    strNum.reverse()    # 뒤집고 None을 반환
    
    # ['0','0','0','0','1'] -> '00001' -> 1
    revNum = int("".join(strNum))
    
    if (revNum==4*i):
        print("Since 4 * {} is {},".format(i,i*4))
        print("The special number is {}.".format(i))
        break
