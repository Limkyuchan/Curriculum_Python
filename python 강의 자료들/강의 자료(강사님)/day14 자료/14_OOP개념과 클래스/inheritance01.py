class Point2D:
    def __init__(self, x = 0, y = 0):
        print('2D생성자')
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def printPoint2D(self):
        print(f'[x={self.x},y={self.y}]')

class Point3D(Point2D): 
    # Point2D를 상속하여 Point3D정의
    
    def __init__(self, x = 0, y = 0, z = 0):
        print('3D생성자')
        super().__init__(x, y) 
        #Point2D.__init__(self, x, y) 동일
        self.z = z

    def setZ(self, z):
        self.z = z

    def getZ(self):
        return self.z
    
    def printPoint3D(self):
        self.printPoint2D()
        print(f'[z={self.z}]')

p1 = Point2D(10, 20)
p1.printPoint2D()
print()
p2 = Point3D(1, 2, 3)
p2.printPoint2D()
p2.printPoint3D()
