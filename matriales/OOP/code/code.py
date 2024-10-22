# class student():
#     student_name = "Amit"
#     student_age = 20
#     student_GPA = 3.4
#     student_gender = "male"
#     def student_info(x):
#         print("student name ")
# s1=student()
# s1.student_name="Omar"
# print(s1.student_info())



# class person():
#     person_name="omar"
#     person_age=20
#     def student_info(self):
#       print("hello ")
# s1=person()
# s1.person_name="oma"
# print(s1.student_info())
# print(s1.__dict__)
# print(s1)
# print(s1.student_info)



# class student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"hello! {self.name} , your age is {self.age}")
# s1 = student( "omar",20)



# #Abstraction
# from abc import ABC ,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass

# class Bird (Animal):
#     def move(self):
#         print("move from bird")
        
# class cat (Animal):
#     def move(self):
#         print("move from cat")
        
# a = Bird()
# b = cat()
# a.move()
# b.move()


#_____________________________________________________________________________________
#inheritance
#___________

# class Calculator1:
#     def summation (self,n1,n2):
#         return n1 + n2
#     def subtraction(self, n1 , n2):
#         return n1 - n2
#     def multiplication(self , n1 , n2):
#         return n1 * n2
#     def division (self , n1 , n2 ):
#         return n1 / n2
# class Calculator2(Calculator1):
#     def power (self , n1 , n2):
#         return n1**n2
# c = Calculator2()
# print(f" result = {c.subtraction(5,2)}")



# class A():
#     def do_this(self):
#         print("i am A")
# class B(A):
#     pass
# class C():
#     def do_this(self):
#         print("i am C")
# class D(B,C):
#     pass
# x=D()
# x.do_this()