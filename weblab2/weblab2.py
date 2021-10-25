from math import sqrt

class Sphere:
    def __init__(self,x=0,y=0,z=0,r=1):
        self.x=x
        self.y=y
        self.z=z
        self.r=r
    def get_volume(self):
        return (4*3.14*self.r**3)/3
    def get_square(self):
        return (4*3.14*self.r**2)
    def get_radius(self):
        return self.r
    def get_center(self):
        return (self.x, self.y, self.z)
    def set_radius(self,r):
        self.r=r
    def set_center(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def is_point_inside(self,x,y,z,):
        r= sqrt((x-self.x)**2+(y-self.y)**2+(z-self.z)**2)
        return r<=self.r


A = Sphere(1,2,3)
print("Volume is ",A.get_volume())
print("Square is ",A.get_square())
print("Radius is ",A.get_radius())
print("Center x,y,z is ", A.get_center())
A.set_radius(5)
print("New radius is ",A.get_radius())
A.set_center(2,3,4)
print("New center x,y,z is ",A.get_center())
print("This point is inside Sphere", A.is_point_inside(10,10,5))


class Matrix:
    def __init__(self,*args):
        self.matrix = []
        if (len(args)>1):
            for i in args:
                self.matrix.append(i)
        else:
            self.matrix = args[0]

    def __eq__(self,other):
        return self.det() == other.det()

    def __ne__(self,other):
        return self.det() != other.det()

    def __gt__(self,other):
        return self.det() > other.det()

    def __ge__(self,other):
        return self.det() >= other.det()

    def __lt__(self,other):
        return self.det() < other.det()

    def __le__(self,other):
        return self.det() <= other.det()

    def __add__(self,other):
        if (len(self.matrix) == len(other.matrix)) and (len(self.matrix[0]) == len(other.matrix[0])):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j]+=other.matrix[i][j]
            return self.matrix
        else:
            return "matrix sizes are not equal"

    def __mul__(self,other):
        if (len(self.matrix[0]) == len(other.matrix)):
            a = [[0 for i in range(len(self.matrix))] for j in range(len(other.matrix[0]))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        a[i][j] += self.matrix[i][k]*other.matrix[k][j]
            return a
        else:
            return "column number of first matrix and row number of second are not equal"

    def min(self, column, row):
        a =[]
        for i in range(len(self.matrix)):
            if i!=column :
                a.append([
                    self.matrix[i][j]
                    for j in range(len(self.matrix[i]))
                    if (j!=row)
                    ])
        return a

    def det(self):
        if len(self.matrix[0])>len(self.matrix):
            l = len(self.matrix)
        else:
            l = len(self.matrix[0])
        det =0
        if l==2:
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        else:
            for i in range(l):
                a = Matrix(self.min(0,i))
                det += (-1)**i*self.matrix[0][i]*a.det()
            return det

a = Matrix([1,2,3],[3,2,1],[2,1,2],[5,5,1])
b = Matrix([1,2,3,4],[3,2,1,0],[2,1,2,-2])
print(a.det())
print(a<=b)
print(a*b)

