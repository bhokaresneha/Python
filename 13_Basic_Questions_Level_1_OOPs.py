'''

##OOPs
##1.Shape class for different shapes.
    ##a. There should be a base class which have.
    ##Attribute: Name of shape.
    ##Methods: Area, Parameter, details of shape

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass   # to be implemented by child class

    def perimeter(self):
        pass   # to be implemented by child class

    def details(self):
        print(f"Shape Name: {self.name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter /circumference: {self.perimeter()}")

    ##b. A rectangle class which inherit the shape class for its method.
    ##Attributes: Length and breadth.
    ##Method : Area, Parameter, details.

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    ##c. A rectangle class which acquires the properties of shape.
    ##Attributes : side
    ##Method : Area, Parameter, details.

class Rectangle1(Shape):

    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.sides=[length,width]

    def area(self):
        return self.sides[0]*self.sides[1]

    def perimeter(self):
        return 2*(self.sides[0]+self.sides[1])

    ##d. A circle class.
    ##Attributes : radius, Pi
    ##Method : area, circumference, details.




class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self): #2*pi*r
        return 2 * 3.14 * self.radius

    ##e. Triangle class (Derived from Shape)
    ## Attributes: side1, side2, side3
    ## Methods: area, perimeter, display

class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        super().__init__("Triangle")
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def area(self):
         s=(self.side1+self.side2+self.side3)/2   
         return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1+self.side2+self.side3

rect = Rectangle(10, 5)
rect.details()

print()

rect1=Rectangle1(10,5)
rect.details()

print()

circle = Circle(7)
circle.details()
            
print()
triangle= Triangle(3,4,5)
triangle.details()




'''
##2. Create a Students marks management system.
##a) Store all the data into a list.
##b) Add a new student
##c) Search a student base on roll number.
##d) Show all the students details stored.
##e) Delete the student details with respect to roll number.
##f) Update the student marks with respect to roll number


class Student():
    def __init__(self,rollno,name,age,marks):
        self.rollno=rollno
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print(f"Rollno: {self.rollno}Name: {self.name},Age: {self.age}, Marks: {self.marks}")

class StudentManagement():

    def __init__(self):
        self.student_record=[]
       

    def add_student(self,rollno,name,age,marks):
        
        s=Student(rollno,name,age,marks)
        self.student_record.append(s)
        print("Student Record added sucessfully..........")

    def search(self,rollno):
         for student in self.student_record:
             if student.rollno==rollno:
                    student.display()
                    return
         print("Student not found ....")                   

    def show_details(self):

        for student in self.student_record:
            print(f"\nRollno:{student.rollno} \nName:{student.name} \nAge:{student.age}\nmarks:{student.marks}")

    def delete_student_details(self,rollno):

        for student in self.student_record:
            if student.rollno==rollno:
                self.student_record.remove(student)
                print("record deleted sucessfully...")
                return
        print("Student not found.....")

    def update_details(self,rollno,new_marks):

        for student in self.student_record:
            if student.rollno==rollno:
                student.marks=new_marks
                print("record updated sucessfully...")
                return
            print("Student not found.....")

    def filestore(self):
        file=open("StudentManagement.txt",mode='a')
        for student in self.student_record:
            file.write(f"\nRollno:{student.rollno}\tName:{student.name}\tAge:{student.age}\tmarks:{student.marks}")
        file.close
        print("done...........")
        
sm=StudentManagement()
print("***************** Student Management ******************")

while True:
    print("\nwhich operation you want to perform=>")
    print("\n1.Add new Student\t2.Serach\t3.Display student Details \n4.delete \t5.update details \t6.Exit")
    choice=int(input("Enter your choice =>"))

    if choice==1:
      
        rno=int(input("Enter roll number=>"))
        name=input("Enter name =>")
        age= int(input("Enter age =>"))
        marks=int(input("Enter Marks=>"))
        sm.add_student(rno,name,age,marks)
      
    elif choice==2:
        rno=input("Enter roll number=>")
        sm.search(rno)

    elif choice==3:
        sm.show_details()

    elif choice==4:
        rno=input("Enter roll number=>")
        sm.delete_student_details(rno)

    elif choice==5:
        rno=input("Enter roll number=>")
        marks=input("Enter Marks")
        sm.update_details(rno,marks)

    elif choice==6:
            sm.filestore()
            print("Exit")
            break


