class Employee:
    language = "python" 
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically  called
        self.name = name
        self.salary = salary
        self.language = language 
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


harry = Employee("Harry", 1300000, "javascript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

# rohan = Employee()