class Rectangle:
    def __init__(self, width=1,height=1):
        self._width = width # °´Ã¼ º¯¼ö
        self._height = height # °´Ã¼ º¯¼ö
    
    def setWidth(self,width):
        self._width = width

    def setHeight(self,height):
        self._height = height
    
    def getWidth(self):
        return self._width
    
    def getHeight(self):
        return self._height

    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2* (self._width + self._height)
    
    def __str__(self):  # state-representation methods
        return ("Width : "+ str(self._width) +"\nHeight : "+str(self._height))

