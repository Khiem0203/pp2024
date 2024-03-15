import math
import numpy as np
import domain.Students as Students
import domain.Courses as Courses
import domain.Mark as Students_mark

students = []
courses = []
marks = []

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
            mark = math.floor(float(mark)) 
            course.setStudent_in_course(Students_mark(course, student, mark))
            print(f"{student.getName()}'s mark for {course.getName()} course: {mark}")