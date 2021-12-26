from flask import Flask, request
from app.models import Student
from app import app, db

@app.route('/students')
def allstudents():
    students  = Student.query.all()

    output = []
    for student in students:
        student_data = {'Student Name': student.name, 'Roll Number': student.rollno}

        output.append(student_data)

    return {"students": output}


@app.route('/stu/<id>')
def get_student(id):
    stu = Student.query.get_or_404(id)
    return {"Student Name": stu.name, "Roll no":stu.rollno, "City":stu.city}


@app.route('/addstudent', methods=['POST'])
def addstudent():
    student = Student(name = request.json['name'], rollno = request.json['rollno'], city = request.json['city'])
    db.session.add(student)
    db.session.commit()
    return {'id':student.id}


@app.route('/updatestudent/<id>', methods=['PUT'])
def updatestudent(id):
    student = Student.query.get(id)
    student.name = request.json['name']
    student.rollno = request.json['rollno']
    student.city = request.json['city']
    db.session.add(student)
    db.session.commit()
    return {'message':"Record Updated"}


@app.route('/deletestudent/<id>', methods=['DELETE'])
def deletestudent(id):
    student = Student.query.get(id)
    if student is None:
        return {"error": "Not Found"}

    db.session.delete(student)
    db.session.commit()
    return {"message":"Record Deleted"}


