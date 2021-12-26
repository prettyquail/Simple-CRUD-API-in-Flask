from app import db


class Student(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(25),nullable = False )
    rollno = db.Column(db.Integer, unique=True, nullable = False )
    city = db.Column(db.String(25),nullable = False )

