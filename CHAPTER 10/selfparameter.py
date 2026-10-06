class Employee:
    language = "python" 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("good morning")

harry = Employee()
harry.language = "javascript"
harry.greet()
harry.getInfo()
# Employee.getInfo(harry)            