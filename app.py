from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_learning.db'  # SQLite database
db = SQLAlchemy(app)

# Database Models
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    student = db.relationship('Student', backref='enrollments')
    course = db.relationship('Course', backref='enrollments')

# Create the database tables
with app.app_context():
    db.create_all()

# Helper function to serialize objects
def serialize_course(course):
    return {
        "courseId": course.course_id,
        "name": course.name,
        "description": course.description,
        "price": course.price
    }

def serialize_student(student):
    return {
        "studentId": student.student_id,
        "name": student.name,
        "email": student.email
    }

def serialize_enrollment(enrollment):
    return {
        "studentId": enrollment.student.student_id,
        "studentName": enrollment.student.name,
        "studentEmail": enrollment.student.email,
        "courseId": enrollment.course.course_id,
        "courseName": enrollment.course.name,
        "coursePrice": enrollment.course.price
    }

# Routes

# Add Course
@app.route('/add_course', methods=['POST'])
def add_course():
    data = request.get_json()
    course_id = data.get('courseId')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not all([course_id, name, description, price]):
        return jsonify({"error": "Missing required fields"}), 400

    if Course.query.filter_by(course_id=course_id).first():
        return jsonify({"error": "Course ID already exists"}), 400

    new_course = Course(course_id=course_id, name=name, description=description, price=price)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course added successfully", "course": serialize_course(new_course)}), 201

# Add Student
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    student_id = data.get('studentId')
    name = data.get('name')
    email = data.get('email')

    if not all([student_id, name, email]):
        return jsonify({"error": "Missing required fields"}), 400

    if Student.query.filter_by(student_id=student_id).first():
        return jsonify({"error": "Student ID already exists"}), 400

    if Student.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    new_student = Student(student_id=student_id, name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added successfully", "student": serialize_student(new_student)}), 201

# Enroll Student in Course
@app.route('/enroll_student', methods=['POST'])
def enroll_student():
    data = request.get_json()
    student_id = data.get('studentId')
    course_id = data.get('courseId')

    if not all([student_id, course_id]):
        return jsonify({"error": "Missing required fields"}), 400

    student = Student.query.filter_by(student_id=student_id).first()
    course = Course.query.filter_by(course_id=course_id).first()

    if not student or not course:
        return jsonify({"error": "Student or Course not found"}), 404

    if Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first():
        return jsonify({"error": "Student is already enrolled in this course"}), 400

    new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(new_enrollment)
    db.session.commit()

    return jsonify({"message": "Student enrolled successfully", "enrollment": serialize_enrollment(new_enrollment)}), 201

# Get All Courses
@app.route('/get_courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([serialize_course(course) for course in courses]), 200

# Get All Students
@app.route('/get_students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([serialize_student(student) for student in students]), 200

# Get All Enrolled Students
@app.route('/get_enrolled_students', methods=['GET'])
def get_enrolled_students():
    enrollments = Enrollment.query.all()
    return jsonify([serialize_enrollment(enrollment) for enrollment in enrollments]), 200

# Delete Course
@app.route('/delete_course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
        return jsonify({"error": "Course not found"}), 404

    # Delete associated enrollments
    Enrollment.query.filter_by(course_id=course_id).delete()
    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"}), 200

# DeleteStudent
@app.route('/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404

    # Delete associated enrollments
    Enrollment.query.filter_by(student_id=student_id).delete()
    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
