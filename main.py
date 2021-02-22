import os
from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime
import pymongo
from dotenv import load_dotenv

load_dotenv()
DBURL = os.getenv("DBURL")

mongo = pymongo.MongoClient(DBURL, maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'attendance')

app = FastAPI()

class Student(BaseModel):
    name: str
    srn: str
    semester: Optional[float] = None

class Student_Min(BaseModel):
    name: Optional[str] = None
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
    
@app.put("/attend", status_code=200)
async def student_attendance(student: Student_Min, response: Response):
    json_student = jsonable_encoder(student)
    srn = json_student['srn'].upper()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        print("hi")
        # TODO send the data to db
    except:
        response.status_code = 403

@app.get("/student", status_code=200)
async def get_attendance(student: Student, response: Response):
    json_student = jsonable_encoder(student)
    srn = json_student['srn'].upper()
    try:
        print("works")
        # TODO send the data to db
    except:
        response.status_code = 403
