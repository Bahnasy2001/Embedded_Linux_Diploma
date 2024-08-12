class Point:

    def __init__(self,xCoord=0,yCoord=0):
        self.xCoord = xCoord
        self.yCoord = yCoord

    #overload + operator
    def __add__(self, point_ov):
        return Point(self.xCoord + point_ov.xCoord,self.yCoord + point_ov.yCoord)
    
point1 = Point(2, 4)
point2 = Point(12, 8)
point3 = point1+point2
print(point3.xCoord)
