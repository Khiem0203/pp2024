students = []
courses = []
marks = []

def number_of_courses():
    num = int(input("Enter number of courses: "))
    return num

def course_info():
    code = input("Enter course's code: ")
    name = input("Enter course's name: ")
    courses.append({"Course's name: ": name,"Course's code: ": code,"Students in the course: ": {}})

def number_of_students():
    num = int(input("Enter number of students: "))
    return num

def student_info():
    id = input("Enter student's ID: ")
    name = input("Enter student's name: ")
    dob = input("Enter student's date of birth: ")
    list_courses()
    print("Choose the course for student: ")
    course_code = input("Enter the course's code: ")
    for course in courses:
        if course["Course's code: "] == course_code:
            course["Students in the course: "][name] = 0
    students.append({"Student's ID": id, "Student's name: ": name, "Student's date of birth: ": dob})
       
def input_marks():
    print("Input marks: ")
    list_courses()
    course_chosen = input("Enter the course's code: ")
    for course in courses:
        if course["Course's code: "] == course_chosen:
            for k, v in course["Students in the course: "].items():
                mark = int(input(f"Enter mark for {k}: "))
                course["Students in the course: "][k] = f"Mark: {mark}"

def list_students():
    print("List of the students: ")
    for student in students:
        print(student)

def list_courses():
    print("List of courses: ")
    for course in courses:
        print(course)

def main():   
    num_courses = number_of_courses()
    for i in range(num_courses):
        course_info()
        
    num_students = number_of_students()
    for i in range(num_students):
        student_info()
    
    input_marks()
    list_courses()
    list_students()

main()


