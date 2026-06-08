# Create the Dog class
class dog:
 def __init__(self,name,age):
      self.name=name
      self.age=age
 def bark(self):
   print("says Woof!",self.name)
# Create an object
d1 = dog("Buddy",3)
# Call the bark method
d1.bark()