class Employee:
    language = "python" 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "javascript"
#harry.getinfo()
Employee.getInfo(harry)            