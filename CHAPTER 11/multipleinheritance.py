class Employee:
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class coder:
    language = "Python"

    def printlanguages(self):
        print(f"Our language is {self.language}")


class Programmer(Employee, coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printlanguages()
b.showLanguage()