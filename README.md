# Online Learning Platform 📚💻
#### Welcome to the Online Learning Platform! 
This platform is designed to help students and educators manage courses, students, and enrollments efficiently. Whether you're a student looking to enroll in courses or an administrator managing the platform, this system has got you covered! 🎓✨

## Features 🌟
##### User Authentication: Add login/signup functionality for students and admins. 🔐

##### Browse Courses: View all available courses with details like name, description, and price. 📖

##### Enroll in Courses: Enroll in your desired courses with just a few clicks. ✅

##### Manage Profile: Add and update your student profile. 👤

##### Add Courses: Easily add new courses with details like course ID, name, description, and price. ➕📚

##### Add Students: Register new students with their ID, name, and email. ➕👤

##### Enroll Students: Enroll students in specific courses. 📝

##### Delete Courses/Students: Remove courses or students from the system. 🗑️

##### View Enrollments: See a list of all enrolled students along with their course details. 📊

## Technologies Used 🛠️
#### Frontend 🖥️
HTML5: Structure of the web pages.

CSS3: Styling and animations (including Bootstrap for responsive design).

JavaScript: Dynamic content and interactivity.

SweetAlert2: Beautiful alert pop-ups.

Animate.css: Smooth animations for a better user experience.

#### Backend ⚙️

Flask: A lightweight Python web framework.

SQLAlchemy: ORM for database management.

SQLite: Database to store courses, students, and enrollments.

CORS: Handles cross-origin requests for seamless frontend-backend communication.

## How to Run the Project 🚀
#### Prerequisites 📋

Python 3.x

Flask (pip install flask)

Flask-SQLAlchemy (pip install flask-sqlalchemy)

Flask-CORS (pip install flask-cors)

#### Steps to Run 🛠️
Clone the Repository:

###### bash
Copy
git clone https://github.com/your-repo/online-learning-platform.git
cd online-learning-platform
##### -->Set Up the Database:

The database will be automatically created when you run the Flask app for the first time.

##### -->Run the Backend:

###### bash
Copy
python app.py
The backend will start running at http://127.0.0.1:5000.

##### -->Open the Frontend:

Open the index.html file in your browser.

The frontend will communicate with the backend at http://127.0.0.1:5000.

##### -->Start Using the Platform:

Login or Signup to access the platform.

Add courses, students, and enroll students in courses.

## API Endpoints 🌐
#### Courses 📚
Add Course: POST /add_course

Get All Courses: GET /get_courses

Delete Course: DELETE /delete_course/<course_id>

#### Students 👤
Add Student: POST /add_student

Get All Students: GET /get_students

Delete Student: DELETE /delete_student/<student_id>

#### Enrollments 📝
Enroll Student: POST /enroll_student

Get All Enrollments: GET /get_enrolled_students

Screenshots 📸
Homepage 🏠
Homepage

Add Course ➕📚
Add Course

Enroll Student 📝
Enroll Student

## Future Enhancements 🚀

Course Ratings: Allow students to rate and review courses. ⭐

Payment Integration: Integrate payment gateways for course purchases. 💳

Admin Dashboard: Create a dedicated dashboard for administrators. 📊

## Contributors 👥
#### JASWANTH guruguntla- Project Lead 🚀
