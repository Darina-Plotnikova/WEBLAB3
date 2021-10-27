import requests
import linalg
import numpy as np
import math

class Sphere(object):

    def __init__(self, r, x, y, z):
        self.Radius = r
        self.x = x
        self.y = y
        self.z = z
        pass

    def getVolume(self):
        result = (4/3)*math.pi*pow(self.Radius, 3)
        return result
    def getSquare(self):
        result = 4*math.pi*pow(self.Radius, 2)
        return result
    def getRadius(self):
        result = self.Radius
        return result
    def getCenter(self):
        result = tuple()
        result = (self.x, self.y, self.z)
        return result
    def setCenter(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        return print("Координаты центра были изменены")
    def setRadius(self,r):
        self.Radius = r
        return print("Радиус сферы был изменен")
    def isPointInside(self, x, y, z):
        return ((pow((x - self.x), 2) + pow((y - self.y),2) + pow((z - self.z), 2)) < pow(self.Radius, 2))

class Matrix(object):
    def __init__(self, x, y):
        self.matrix = np.matrix([x,y])
        self.deter = np.linalg.det(self.matrix)
        pass
    def __lt__(self, other):
        if self.deter < other.deter:
            return True
        else: return False    
    def __le__(self, other):
        if self.deter <= other.deter:
            return True
        else: return False  
    def __eq__(self, other):
        if self.deter == other.deter:
            return True
        else: return False  
    def __ne__(self, other):
        if self.deter != other.deter:
            return True
        else: return False  
    def __gt__(self, other):
        if self.deter > other.deter:
            return True
        else: return False  
    def __ge__(self, other):
        if self.deter >= other.deter:
            return True
        else: return False
    def __add__(self, other):
        return self.matrix + other.matrix
    def __mul__(self, other):
        return self.matrix*other.matrix
    

class Client(object):

    def __init__( self, host, session = requests.Session() ):
        self.session = session
        self.host = host
        pass
    def __del__(self):
        self.session.close()
        pass

client = Client("https://httpbin.org/cookies")
sphere = Sphere(4, 0,0,0)
m1 = Matrix ([1,2],[3,4])
m2 = Matrix ([3,4],[5,6])

r = client.session.get(client.host)
print(r.content)
print(sphere.getRadius())
print(sphere.getCenter())
print(sphere.getVolume())
print(sphere.getSquare())
print(m1 > m2)
print(m1 < m2)
print(m1 == m2)
print(m1 != m2)
print(m1 <= m2)
print(m1 >= m2)
print(m1 + m2)
print(m1 * m2)




