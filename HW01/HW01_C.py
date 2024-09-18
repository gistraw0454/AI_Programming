totalSum = 0
for odd in range(1,1000000,2):
    
    numSum = 0
    for i in str(odd):
        numSum += int(i)
    totalSum += numSum

print("The sum of the digits of odd numbers\nFrom 1 to one million is {:,}.".format(totalSum))