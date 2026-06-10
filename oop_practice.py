# # Create the Dog class
# class dog:
#  def __init__(self,name,age):
#       self.name=name
#       self.age=age
#  def bark(self):
#    print("says Woof!",self.name)
# # Create an object
# d1 = dog("Buddy",3)
# # Call the bark method
# d1.bark()
# class Person:
#   species = "Human" # Class property

#   def __init__(self, name):
#     self.name = name # Instance property

# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)
# class Person:
#   lastname = ""

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes"

# print(p1.lastname)
# print(p2.lastname)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name} ({self.age})"

# p1 = Person("Tobias", 36)
# print(p1)
# class car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
# c1=car("Toyota","Camry",2024)
# c2=car("Honda","City",2023)
# print(vars(c1),vars(c2))
# or we can use print(c1.__dict__)
# best way to use 
# def __str__(self):
#return f"car(brand={self.brand},model={self.model},year={self.year})

# Q2
# class rectangle:
#     def Area(self,length,width):
#         return length*width
# A=rectangle()
# print(A.Area(5,6))

# Q3
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
        
#         if self.marks>=40:
#             return "pass"
#         else:
#             return "fail"
# s1=student("kaushal",67)
# print(s1.result(),s1.name)

# Q4
# class aircraft:
#     def __init__(self,name,speed,range):
#         self.name=name
#         self.speed=speed
#         self.range=range
#     def __str__(self):
#         return f"name={self.name},speed={self.speed},range={self.range}"
# a1=aircraft("Rafaele",1912,3700)
# print(a1)

# Q5

# class bank:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(self.balance)
#     def withdraw(self,amount):
#         self.balance-=amount
#         print(self.balance)
# a1=bank("ayush",5000)
# a1.withdraw(2000)

# Q6
# class aircraft:
#     def __init__(self,name,speed,range):
#         self.name=name
#         self.speed=speed
#         self.range=range
#     def __str__(self):
#         return f"name={self.name},speed={self.speed},range={self.range}"
    
# A1=[["Rafaele",1912,3700],["Tejas",2205,3000]]
# for i in A1:
    
#     A2=aircraft(*i)
#     print(A2)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)