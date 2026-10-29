import math

class Point:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

try:
    p = Point(3, 4)
    assert (p.x, p.y) == (3, 4)
    assert p.norm() == 5.0
    assert repr(p) == "Point(3, 4)"
    q = Point(0, 1)
    assert (q.x, p.x) == (0, 3)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

p = Point(3, 4)
print(p.norm())
print(Point.norm(p))
print(p)

# Questions échauffement 2:
# 1) Le print donne le même résultat
# 2) On obtient une type error
# 3) Il s'affiche  <__main__.Point object at 0x00000127A72ECA50> --> renvoie le type de l'objet

class Bad:
    items = []

    def add(self, x):
        self.items = []
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)

# Question échauffement 3:
# 1) b voit l'élément ajouté à a car items est défini pour toute la classe --> attribut de classe

class Tirelire:
    pieces=[]
    def __init__(self):
        self.pieces=[]
    def deposit(self, value: float):
        if value > 0:
            self.pieces.append(value)
        else :
            raise ValueError
    def __len__(self):
            return len(self.pieces)
    def total(self):
        s=0
        for p in self.pieces:
            s+=p
        return s
    def __repr__(self):
        return f"Tirelire({len(self)} coins, total={self.total()}0)"

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name=first_name
        self.last_name=last_name
        self.Grade={}

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, Grade = {self.Grade})"

try:
    student = Student("Achille", "Talon")
    r = repr(student)
    assert isinstance(r, str), "__repr__ must return a str"
    assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
except Exception as e:
    print('OOPS - There is an issue in your code.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


