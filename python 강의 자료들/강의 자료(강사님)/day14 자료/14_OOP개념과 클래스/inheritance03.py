class Point2D:
    def __init__(self, x = 0, y = 0):
        print('2D생성자')
        self.x = x
        self.y = y
    def parent(self):
        print('Point2D.parent()')
    
class Point3D(Point2D): # Point2D를 상속하여 Point3D정의
    def __init__(self, x = 0, y = 0, z = 0):
        #super().__init__(x, y) # Java/C++처럼 부모 생성자 자동 호출 안 함
        print('3D생성자')
        self.z = z

    def parent(self):
        print('Point3D.parent()')

    def method(self):
        super().parent() #부모 메서드 호출
   
p = Point3D(1, 2, 3)
p.parent()
p.method()