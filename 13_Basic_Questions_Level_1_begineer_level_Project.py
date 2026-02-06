##Beginner-Level Projects
##1. Student Management System
## - Concepts Should Covered:
##Encapsulation, Basic Inheritance, Abstraction
## - Description:
##Manage student records such as names, grades, and courses. You can perform basic CRUD 
##operations (Create, Read, Update, Delete) for student data.
## - Features:
##a. Create a `Student` class with attributes like `name`, `id`, `grades`.
##b. Implement methods to add, update, and display student data.
##c. Optionally, implement simple inheritance with subclasses like `GraduateStudent` or 
##`UndergraduateStudent`.





class Student():
    def __init__(self,sid,name,grades):

        self.sid=sid
        self.name=name
        self.grades=grades


    def display_data(self):

        print(f"Student Details => \n id=>{self.id}\t Name=>{self.name} \t Grades=>{self.grades}")


class GraduateStudent():
        def __init__(self):
             self.data=[]

        def add_student(self):
            s=Student("1","sneha","A+")
            self.data.append(s)
            print(f"{self.data}Student Record added sucessfully..........")

        def show_details(self):

            for student in self.data:
                print(f"Student Details => \n id=>{student.sid}\t Name=>{student.name} \t Grades=>{student.grades}")
    
            
gs=GraduateStudent()


                
############################################################################################################
##2. Library Management System
## - Concepts Should Covered:
##Encapsulation, Basic Inheritance, Polymorphism
## - Description: 
##Build a system to manage books, patrons, and borrow/return functionality. A simple text-`
##based system to keep track of library items.
## - Features:
##a. `Book` class with attributes like `title`, `author`, and `ISBN`.
##b. `Patron` class to manage users.
##c. Implement methods for borrowing and returning books.
##d. Optionally, extend the `Book` class to different types, such as `Magazine` and 
##`Ebook`.
##3. Banking System
## - Concepts Should Covered:
##Encapsulation, Basic Inheritance
## - Description: 
##A simple banking system that allows users to create accounts, deposit and withdraw 
##money, and transfer funds.
## - Features:
##a. `Account` class with attributes like `account_number`, `balance`, `account_type`.
##b. Methods to deposit, withdraw, and transfer money between accounts.
##c. Optionally, add a `SavingsAccount` subclass with additional features like interest 
##calculation.
