import Rectangle     # class를 import한다.

r = Rectangle.Rectangle(4,5)    # 객체 생성

print(r)    


r = Rectangle.Rectangle()

print(r)

r = Rectangle.Rectangle(4)

print(r)


r = Rectangle.Rectangle()

r.setWidth(4)   # r._width = 4 가능
r.setHeight(5)  # r._height = 5 가능

print(r.getWidth()) # print(r._width) 가능
print(r.getHeight())    #print(r._height) 가능

print(r.area()) 
print(r.perimeter())
