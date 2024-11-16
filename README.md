# Student Management System

This Python project implements a simple student management system using MySQL for data storage.  The system allows for adding, viewing, searching, updating, and deleting student records.  It also includes teacher login and registration functionalities.

## 1. Introduction

This project provides a basic command-line interface (CLI) for managing student information.  It demonstrates fundamental database interactions using MySQL and Python's `mysql.connector` library.  The system is designed for educational purposes and can be expanded to include more advanced features.

## 2. Database Setup

The system interacts with a MySQL database named `studentdb`.  This database contains two tables:

* **studentsinfo:** Stores student information (school ID, name, course, course ID, course marks, phone number).
* **teacher:** Stores teacher credentials (ID, password).


The script creates these tables if they don't exist. **Make sure you have MySQL installed and running before running the script.**  You'll also need to adjust the database connection parameters (host, user, password) in the code to match your MySQL setup.

## 3. Functionality

The system provides the following functionalities:

* **Teacher Login/Registration:** Teachers can log in using their ID and password or register a new account.
* **Add Student:** Allows teachers to add new student records to the database.
* **View Students:** Displays all student records or a specific student's records based on school ID.
* **Search Student:** Searches for a student by school ID.
* **Update Student:** Updates the details of an existing student record.
* **Delete Student:** Deletes a student record.
* **Student Login:** Students can login to view their own information (name, course, grade).


## 4. Code Structure

The code is organized into several functions, each responsible for a specific task:

* `add_student()`: Adds a new student.
* `view_students()`: Displays all student records.
* `sview_students()`: Displays a specific student's records (for student login).
* `search_student()`: Searches for a student.
* `update_student()`: Updates student information.
* `delete_student()`: Deletes a student record.
* `exit_program()`: Exits the program.
* `display_menu()`: Displays the main menu.
* `register()`: Registers a new teacher account.
* `login()`: Handles teacher login.
* `slogin()`: Handles student login.
* `start()`: Displays the initial menu (student/teacher login).
* `tstart()`: Handles teacher login/registration menu.


## 5. How to Run

1. **Install mysql.connector:** `pip install mysql-connector-python`
2. **Configure Database:** Make sure MySQL is running and update the database connection details (host, user, password) in the script.
3. **Run the script:** Execute the Python script.  The program will start with a menu allowing you to choose between student or teacher login.


## 6.  Dependencies

* `mysql.connector`


## 7. Limitations

* **Security:** The current password storage is insecure.  For a production system, use appropriate hashing and salting techniques.
* **Error Handling:** Error handling is basic.  More robust error checks (e.g., input validation, database error handling) should be added.
* **Input Validation:**  The code lacks input validation to prevent SQL injection vulnerabilities.  Parameterized queries should be used to prevent SQL injection attacks.
* **Scalability:** This system is not designed for a large number of users or concurrent access.



## 8. Future Improvements

* Implement more robust error handling and input validation.
* Add parameterized queries to prevent SQL injection.
* Improve security by using proper password hashing and salting.
* Consider using a more user-friendly interface (e.g., a graphical user interface).
* Add features like reporting, data export, and more sophisticated search capabilities.


This README provides a comprehensive overview of the student management system.  Remember to always prioritize security best practices when working with databases.  The use of parameterized queries is strongly recommended to protect against SQL injection vulnerabilities.
