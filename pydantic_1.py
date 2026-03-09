# Student Management System
# Python is dynamically typed language
# DRY : Dont repeat yourself



# def create_student(name:str,age:int,college:str):

#     if type(name)==str and type(age)== int and type(college)==str:
#         print(name)
#         print(age)
#         print(college)
#         print('Student Created')
#     else:
#         raise TypeError("Invalid Data Type")

    

# create_student('Shishir',20,'abcd')

# Pydantic Data Validation
# Type Validation
# Field Validation

from pydantic import BaseModel,Field

class Student(BaseModel):
    name: str
    age: int = Field (gt =0,le=100)
    college: str = None
    marks: float = Field(default= 0.0, ge =0 , le =100)

student_info = {'name': 'Shishir', 'age': 80, 'college': 'Masai'}

# using this student_info dict create student object

student= Student(**student_info)

print(student.marks)
