  
"""class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname)
    print(self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()"""


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname)
    print(self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    Person.__init__(self,fname,lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear) 
x.printname()


"""class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname)
    print(self.lastname)
class Student(Person):
  def __init__(self, fname, lname,year ):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear) 
x.printname() """

"""class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class College(Person):
  def __init__(self, fname, lname, college):
     super().__init__(fname, lname)
     self.college = college
  def printn(self):
    print(self.firstname,self.lastname,self.college)
  
class Student(College):
  def __init__(self,fname,lname,class1,degree):
    super().__init__(fname,lname,class1)
    self.Degree=degree

mani=Student("Mani","Kandan","abc","M.E")
mani.printname()
mani.printn()
print(mani.Degree)"""

# Python example to show the working of multiple
# inheritance

class Base1():
	def __init__(self):
		self.str1 = "a"
		print("Base1")


class Base2():
	def __init__(self):
		self.str2 = "b"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
