class Student:
    def __init__(self):
        self.id = ""
        self.age = 0
        self.marks = 0

    def setID(self, id):
        self.id = id
    
    def setMarks(self, marks):
        self.marks = marks

    def setAge(self, age):
        self.age = age
    
    def validateMarks(self):
        if self.marks >= 0 and self.marks <= 100:
            return True
        return False

    def validateAge(self):
        if self.age >= 20:
            return True
        return False

    def checkQualification(self):
        if self.validateAge() and self.validateMarks() and self.marks >= 65:
            return True
        return False

    def getId(self):
        return self.id

    def getAge(self):
        return self.age

    def getMarks(self):
        return self.marks


student = Student()
student.setID(input("Enter student ID "))
student.setAge(int(input("Enter student age ")))
student.setMarks(int(input("Enter student marks ")))
if student.checkQualification():
    print("Qualified")
else:
    print("Not qualified")