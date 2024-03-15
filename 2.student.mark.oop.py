students = []
courses = []
marks = []

class Students:
    def __init__(self):
        self.__id = input("Enter Student's ID: ")
        self.__name = input("Enter Student's Name: ")
        self.__dob = input("Enter Student's Date of Birth: ")
        self.marks = [] 
    
    def getID(self):
        return self.__id
    def setID(self, id):
        self.__id = id
    
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    
    def getDOB(self):
        return self.__dob
    def setDOB(self, dob):
        self.__dob = dob
        
    def __str__(self):
        return f"Student's information: ID: {self.__id},Name: {self.__name},DOB: {self.__dob}."

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

class Students_mark:
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark
        
    def __str__(self):
        return f"Mark for course {self.course.getName()} of student {self.student.getName()}: {self.mark}"
    
    def getCourse(self):
        return self.course
    def setCourse(self,course):
        self.course = course
    
    def getStudent(self):
        return self.student
    def setChoose_student(self,student):
        self.student = student
    
    def getMark(self):
        return self.mark
    def setMark(self, mark):
        self.mark = mark       
           
def number_of_courses():
    num = int(input("Enter number of Courses: "))
    return num
num_courses = number_of_courses()
for i in range(num_courses):
    course = Courses()
    courses.append(course)

def number_of_students():
    num = int(input("Enter number of Students: "))
    return num
num_students = number_of_students()
for i in range(num_students):
    student = Students()
    students.append(student)
    print("Choose Course for Student: ")
    for i in range(num_courses):
        print(courses[i])
    course_code = input("Enter the Course's Code: ")
    for course in courses:
        if course.getCode() == course_code:
            mark = input("Enter mark for the student: ") 
            course.setStudent_in_course(Students_mark(course, student, mark))
            print(f"{student.getName()}'s mark for {course.getName()} course: {mark}")

def main():                   
    print("List of students: ")
    for student in students:
        print(student)
    
    print("List of courses: ")
    for course in courses:
        print(course)
        
    print("Student's marks: ")
    for course in courses:
        for student_mark in course.getStudent_in_course():
            print(student_mark)

main()
