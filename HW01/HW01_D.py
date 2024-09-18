coefficient = float(input("Enter coefficient of restitution: "))    # .9 -> 0.9
height = float(input("Enter initial height in meters: "))

bounces=0
distances=0
while height >= 0.1:
    distances += height
    height *= coefficient
    bounces+=1

    if(height>=0.1):
        distances += height

print("Number of bounces: {}".format(bounces))
print("Meters traveled: {:.2f}".format(distances))