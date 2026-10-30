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
# 2) Il faut définir la liste dans la fonction init pour que chaque instance ait sa propore liste

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
        for p in self.pieces:   # on parcourt la liste des pièces
            s+=p
        return s
    def __repr__(self):
        return f"Tirelire({len(self)} coins, total={self.total()})"

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name=first_name
        self.last_name=last_name
        self.grades=defaultdict(list)

    def add_grade(self, course: str, grade: float):
        if 0 <= grade <= 20:            # on vérifie que la note est valide (comprise entre 0 et 20)
            self.grades[course].append(grade)       # on ajoute la note à la liste correpondant au cours "course" dans le dictionnaire
        else:
            raise ValueError
        
    def followed_topics(self):
        return list(self.grades.keys())
    
    def compute_average(self, course: str):
        if course in self.grades:
            return sum(self.grades[course])/len(self.grades[course])     # on somme les notes puis on divise par le nombre de notes (= longueur de la liste)
        else:
            raise ValueError
        
    def report(self):
        lignes=[f"Report for student {self.first_name} {self.last_name}"
                ,f"+===============+===============+",
                f"|     Topic     |    Average    |", 
                f"+===============+===============+" ]      # initialisation du bulletin avec les premières lignes
        sep = f"+---------------+---------------+"      # ligne de séparation entre les matières
        for topic in self.grades.keys():
            average= self.compute_average(topic)
            lignes.append(f"|{topic:^15}|{average:^15.2f}|")    # pour chaque matière, on récupère la moyenne de l'élève et on crée la ligne correspondante
            lignes.append(sep)
        return "\n".join(lignes) 
    
    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, Grade = {self.grades})"
    


class Classe:
    def __init__(self, classname: str):
        self.classname=classname
        self.grades=defaultdict(list)   # crée automatiquement une liste vide lorsqu'une clé est appelée pour la première fois

    def add_student(self, student: Student):
        self.grades[(student.first_name, student.last_name)]=student

    def __len__(self):
        return len(self.grades.keys())

    def get_student(self, first_name: str, last_name: str):
        return self.grades.get((first_name, last_name)) # le get d'un dictionnaire retourne None si l'élève n'est pas présent dans les clés

    def load_students_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as data:
            for line in data:
                line=line.strip().split(',') # strip pour enlever les espaces/retours à la ligne aux bords et split(",") pour couper la chaine en plusieurs objets lorsqu'ils sont séparés par des virgules
                student=Student(line[0], line[1])   # les 2 premiers éléments correspondent au prénom et au nom de l'élève
                self.add_student(student)

    def load_grades_from_file(self, filename: str): 
         with open(filename, 'r', encoding='utf-8') as data:
            for line in data:
                line=line.strip().split(',')
                student= self.get_student(line[0],line[1])
                if self.get_student(student.first_name,student.last_name) == None:
                    student= Student(line[0],line[1])
                    self.add_student(student)       # si l'élève n'est pas encore dans la classe, on le rajoute
                    raise Warning
                course = line[2]
                for g in line[3:]: # les notes sont les éléments indexés à partir de 3 dans la liste line crée
                    student.add_grade(course,float(g))      # on convertit les notes en float pour pouvoir les ajouter
                    self.grades[(line[0],line[1])]=student

    def catalog (self):
        cat=defaultdict(int)    # la première fois qu'une clé est appelée, sa valeur s'initialise à 0
        for student in self.grades.values():    # on parcourt la liste des élèves de la classe
            for course in student.followed_topics():    # puis les sujets qu'ils étudient
                cat[course]+=1
        return cat

    def compute_averages(self):
        dic= defaultdict(int)
        for student in self.grades.values(): # on parcourt les élèves et les cours pour entrer la somme des moyennes de chaque cours dans le dictionnaire
            for course in student.followed_topics():
                avg = student.compute_average(course)
                dic[course]+=avg
        cat = self.catalog()
        for course, nb in cat.items():
            dic[course]=dic[course]/nb      # pour chaque cours, on divise la somme calculée par le nombre d'élèves dans le cours (obtenu grace à la méthode catalog)
        return dic

    def detailed_report(self, student: Student | None):
        if student is None: 
            return "Student not found in the class."
        lignes=[f"Detailed Report for student {student.first_name} {student.last_name}"
                        ,f"+===============+===============+===============+",
                        f"|     Topic     |    Average    |   Class Avg   |", 
                        f"+===============+===============+===============+" ]
        sep = f"+---------------+---------------+---------------+"
        avgs= self.compute_averages()        
        for topic in student.grades.keys(): # on reprend la structure de la méthode report de Student en ajoutant une colonne pour la moyenne de la classe, que l'on récupère grâce à la méthode compute_averages
            average = student.compute_average(topic)
            class_avg = avgs[topic]
            lignes.append(f"|{topic:^15}|{average:^15.2f}|{class_avg:^15.2f}|")
            lignes.append(sep)
        return "\n".join(lignes)
               
    def __repr__(self):
        return f"Class({self.classname}, Students:{list(self.grades.values())})"




