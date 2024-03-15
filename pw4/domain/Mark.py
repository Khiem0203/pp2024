students = []
courses = []
marks = []

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