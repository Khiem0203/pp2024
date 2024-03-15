students = []
courses = []
marks = []

class Courses:
    def __init__(self):
        self.__code = input("Enter Course's Code: ")
        self.__name = input("Enter Course's Name: ")
        self.__student_in_course = []
    
    def getCode(self):
        return self.__code
    def setCode(self, code):
        self.__code = code
        
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    
    def getStudent_in_course(self):
        return self.__student_in_course
    def setStudent_in_course(self,student_in_course):
        self.__student_in_course.append(student_in_course)
        
    def __str__(self):
        return f"Course's information: Code: {self.__code},Name: {self.__name}."