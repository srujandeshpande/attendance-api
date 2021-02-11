from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    srn: str
    semester: Optional[float] = None

@app.get("/")
async def root():
    res = "Hey there! Welcome to the Attendance App of PESU I/O Course 'Cloud Native Full Stack Development'"
    return res

@app.post("/student", status_code=201)
async def new_student(student: Student, response: Response):
    json_student = jsonable_encoder(student)
    try:
        print("works")
        # TODO send the data to db
    except:
        response.status_code = 403
    
    
