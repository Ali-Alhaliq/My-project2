from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],   # ← كان فيها خطأ
    allow_headers=["*"]
)
class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="ali", grade=5),
    Student(id=2, name="laith", grade=2)
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student:Student):
    students.append(new_student)
    return new_student
@app.put("students/{student_id}")
def update_student(student_id:int,update_student:Student):
    for index,Student in enumerate(students):
        if student_id == student_id:
            students[index]=update_student
            return update_student
    return { "error ":"student not found"}
@app.delete("students/{student_id}")
def delet_student(student_id:int):
    for index,Student in enumerate(students):
        if student_id == student_id:
            del students[index]
            return{"message":"Student delet"}
    return{"error":"steudent not found"}








