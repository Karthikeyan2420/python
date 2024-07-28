"""class Students:
   def __init__(self, name,rank, points):
      self.name = name

   def gettername(self):
      print(self.name)

   def settername(self,name):
      self.name=name
      
# create 4 objects:
st1 = Students("Steve","first", 100)

st1.gettername()
st1.settername("harish")
st1.gettername()"""

class Employee:
    def __init__(self, name, id, salary, project):
        self.name = name
        self.id = id
        self.salary = salary
        self.project = project

    def show_sal(self):
        print("Name: ", self.name, "Salary:", self.salary)
 
    def proj(self):
        print(self.name, 'is working on', self.project)
 
emp = Employee('James', 102 , 100000 , 'Python')
emp.show_sal()
emp.proj()

