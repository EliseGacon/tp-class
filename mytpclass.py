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
    def __init__(self):
        self.items = []
    def add(self, x):
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
        self.grades=defaultdict(list)

    def add_grade(self, course: str, grade: float):
        if 0 <= grade <= 20:
            self.grades[course].append(grade)
        else:
            raise ValueError
        
    def followed_topics(self):
        return list(self.grades.keys())
    
    def compute_average(self, course: str):
        if course in self.grades:
            return sum(self.grades[course])/len(self.grades[course])
        else:
            raise ValueError
    def report(self):
        lignes=[f"Report for student {self.first_name} {self.last_name}"
                ,f"+===============+===============+",
                f"|     Topic     |    Average    |", 
                f"+===============+===============+" ]
        sep = f"+---------------+---------------+"
        for topic in self.grades.keys():
            average= self.compute_average(topic)
            lignes.append(f"|{topic:^15}|{average:^15.2f}|")
            lignes.append(sep)
        return "\n".join(lignes)
    
    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, Grade = {self.grades})"
    


class Classe:
    def __init__(self, classname: str):
        self.classname=classname
        self.grades=defaultdict(list)

    def add_student(self, student: Student):
        self.grades[(student.first_name, student.last_name)]=student

    def __len__(self):
        return len(self.grades.keys())

    def get_student(self, first_name: str, last_name: str):
        return self.grades.get((first_name, last_name))

    def load_students_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as data:
            for line in data:
                line=line.strip().split(',')
                student=Student(line[0], line[1])
                self.add_student(student)

    def load_grades_from_file(self, filename: str): 
         with open(filename, 'r', encoding='utf-8') as data:
            for line in data:
                line=line.strip().split(',')
                student= Student(line[0],line[1])
                if self.get_student(student.first_name,student.last_name) == None:
                    raise Warning
                course = line[2]
                for g in line[3:]:
                    student.add_grade(course,float(g))
                    self.grades[(line[0],line[1])]=student
                print(self.get_student(student.first_name,student.last_name)) #pb: on recrée un dictionnaire à 
                # chaque fois pour l'élève : si l'élève est présent dans plusieurs cours, on a au final un dictionnaire avec 
                # seulement la dernière matière appelée

    def catalog (self):
        cat=defaultdict(int)
        for student in self.grades.values():
            for course in student.followed_topics():
                cat[course]+=1
        return cat
            
    def __repr__(self):
        return f"Class({self.classname}, Students:{list(self.grades.values())})"





# pour tester

import io
import contextlib


classe = Classe("P1920")
classe.load_students_from_file('classe.csv')
classe.load_grades_from_file('grades.csv')
print(classe.get_student("Enrico", "Fermi"))
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    classe.load_grades_from_file('grades.csv')
    
assert classe.get_student("Albert", "Einstein").compute_average("Physics") == 13.25
assert classe.get_student("Enrico", "Fermi").compute_average("Mathematics") == 12.5
assert classe.get_student("Enrico", "Fermi").compute_average("English") == 15.5
