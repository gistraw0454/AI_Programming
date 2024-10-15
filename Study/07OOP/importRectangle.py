import Rectangle

r = Rectangle.Rectangle(4,5)

print(r)


r = Rectangle.Rectangle()

print(r)

r = Rectangle.Rectangle(4)

print(r)


r = Rectangle.Rectangle()

r.setWidth(4)   # r._width = 4
r.setHeight(5)  # r._height = 5

print(r.getWidth()) # print(r._width)
print(r.getHeight())    #print(r._height)

print(r.area()) 
print(r.perimeter())
