import math
import numpy as np

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

    def getMarks(self):
        return self.marks
    
    def calculate_GPA(self):
        if len(self.marks) == 0:
            return 0
        else:
            return np.mean([float(mark.mark) for mark in self.marks])

    def __str__(self):
        return f"Student's information: ID: {self.__id},Name: {self.__name},DOB: {self.__dob}, GPA: {self.calculate_GPA()}"