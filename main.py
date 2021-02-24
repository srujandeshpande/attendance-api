import os
from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime
import pymongo
from dotenv import load_dotenv
from bson.json_util import dumps
import json

load_dotenv()
DBURL = os.getenv("DBURL")

mongo = pymongo.MongoClient(DBURL, maxPoolSize=50, connect=True)
db = mongo['attendance']

app = FastAPI()

class Student(BaseModel):
    name: str
    srn: str
    semester: Optional[int] = None

class Student_Min(BaseModel):
    srn: str

@app.get("/")
async def root():
    res = "Hey there! Welcome to the Attendance App of PESU I/O Course 'Cloud Native Full Stack Development'"
    return res

@app.get("/students", status_code=200)
async def get_students(response: Response):
    # json_student = jsonable_encoder(student)
    # srn = json_student['srn'].upper()
    students = db['students']
    res = json.loads(dumps(students.find({},{ "_id": 0, "srn": 1, "name": 1, "semester": 1 })))
    return res

@app.post("/students", status_code=201)
async def new_student(student: Student, response: Response):
    json_student = jsonable_encoder(student)
    json_student['srn'] = json_student['srn'].upper()
    students = db['students']
    try:
        students.update({'srn': json_student['srn']}, json_student, upsert=True)
    except:
        response.status_code = 400
    

@app.get("/attendance", status_code=200)
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

@app.put("/attendance", status_code=200)
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

