beginningSal = float(input("Enter beginning salary: "))
newSal = beginningSal*(1.05**4)
print("New salary: ${:,.2f}".format(newSal))
changeSal = (newSal-beginningSal)/beginningSal*100
print("Change: {:.2f}%".format(changeSal))

# ���ڿ� , ��� ��� (float���� ����)
#1. print(format(num, ','))
#2. print('{0:,}'.format(num))
#3. print(f'{num:,}')