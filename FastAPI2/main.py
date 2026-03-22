#pip install fastapi pydantic uvicorn
#uvicorn main:app
#uvicorn main:app --reload
from fastapi import FastAPI,HTTPException,Path, Query
import json

app= FastAPI()

#localhost:8000/hi
@app.get("/hi")
def say_hello():
    return "Hi World"

#localhost:8000/bye
@app.get("/bye")
def say_hello():
    return "Bye World"


@app.get("/students")
def get_all_students():
    with open('student.json','r') as f:
        students_data= json.load(f)
    return students_data


@app.get("/students/{student_id}")
def get_student_by_id(student_id:str= Path(...,)):
    data=get_all_students()
    if student_id not in data:
        raise HTTPException(status_code=404,description="Invalid ID")
    return data[student_id]


@app.get("studentss")
def get_student_by_id(student_id:str= Query(...,)):
    data=get_all_student()
    if student_id not in data:
        raise HTTPException(status_code=404,description="Invalid ID")
    return data[student_id]












# #path parameter
# @app.get("/students/{student_id}")
# def get_student_with_id(student_id:str = Path(..., description="id of student",example="ST001")):
#     data=get_all_students()
#     if student_id not in data:
#         raise HTTPException(status_code=404,detail="Student with mentioned id not found")
#     return data[student_id]

# #query parameter
# @app.get("/studentss")
# def get_student_with_id(student_id:str = Query(...,)):
#     data=get_all_students()
#     if student_id not in data:
#         raise HTTPException(status_code=404,detail="Student with mentioned id not found")
#     return data[student_id]

# data=get_all_students()
# print(data["ST001"]["city"])
    
