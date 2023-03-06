import pandas as pd 
import numpy as np 
from typing import Optional

class Course:
    """A class to hold a single class and calculate the grade"""
    def __init__(self, name: str, credits: int, grade: Optional[str], target_grade: Optional[str]):
        self.name = name
        self.credits = credits
        self.grade = grade
        self.syllabus_items = dict()
    
    def add_syllabus_item(self, name: str, weight: float, grade: Optional[int]):
        self.syllabus_items.update({name: {'weight': weight, 'grade': grade}})
    
    def calculate_grade(self):
        for item in self.syllabus_items:
            self.grade = self.grade + self.syllabus_items[item]['weight'] * self.syllabus_items[item]['grade']

class Semester:
    """A semester is a collection of courses"""

    def __init__(self, name: str):
        self.name = name
        self.courses = []
        self.gpa = 0
        self.credits = 0

    def calculate_gpa(self):
        """Calculate the semester GPA
        
        Parameters
        ----------
        None 

        Returns
        -------
        GPA : float
            The GPA for the semester

        """

    

    def add_course(self, course: Course):
        self.courses.append(course)


class School:

    

    def __init__(self, name):
        self.name = name


            