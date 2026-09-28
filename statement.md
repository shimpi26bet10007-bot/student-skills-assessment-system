# Student Skill Assessment System

## 1. Problem Statement

Students develop different skills like programming, communication, problem solving and technical or subject knowledge but assessing these skills manually can be time-consuming and may make it difficult to identify a student's strengths and areas that require improvement.

The Student Skill Assessment System is a Python-based command-line application dwhich is esigned to provide a structured method for assessing the skills of students. The system collects information of student and skill scores, calculates the overall performance, identifies the strongest and weakest skills, stores assessment records and generates a detailed assessment report.

## 2. Scope of the Project

The scope of the project includes:

- Collecting student information.
- Collecting registration number, email, and course details.
- Assessing multiple student skills.
- Validating skill scores entered by the user.
- Calculating total marks.
- Calculating overall percentage.
- Identifying the strongest skill.
- Identifying the skill requiring improvement.
- Determining the overall performance level.
- Saving student assessment records.
- Viewing previously saved records.
- Generating a detailed assessment report.
- Running the application through the command line.

The system is designed as a Python-based command-line application.

## 3. Target Users

The intended users of the system are:

- College students
- Teachers and instructors
- Academic mentors
- Training and placement coordinators

## 4. High-Level Features

### 4.1 Student Management

The system collects and manages:

- Student name
- Registration number
- Email
- Course

### 4.2 Skill Assessment

The system assesses the following skills:

- Programming
- Communication
- Problem Solving
- Technical/Subject Knowledge

Each skill is evaluated on a scale of 0 to 10.

### 4.3 Input Validation

The system validates user input and prevents invalid skill scores.

Valid scores must be between 0 and 10.

The system also handles invalid numerical input without terminating unexpectedly.

### 4.4 Performance Analysis

The system:

- Calculates total marks.
- Calculates overall percentage.
- Identifies the strongest skill.
- Identifies the skill requiring improvement.
- Determines the overall performance level.

### 4.5 Data Storage

Student assessment records are stored in a JSON file.

The system can retrieve and display previously saved student records.

### 4.6 Report Generation

The system generates a detailed text-based assessment report containing:

- Student details
- Skill-wise scores
- Total marks
- Percentage
- Performance level
- Strongest skill
- Skill requiring improvement

### 4.7 Command-Line Menu

The application provides a menu-based workflow:

1. Assess Student
2. View Saved Records
3. Exit

## 5. Expected Input

The system accepts:

- Student name
- Registration number
- Email
- Course
- Programming score
- Communication score
- Problem Solving score
- Technical/Subject score

## 6. Expected Output

The system displays:

- Student information
- Skill-wise assessment
- Total marks
- Overall percentage
- Performance level
- Strongest skill
- Skill requiring improvement
- Confirmation of saved records
- Location of the generated report

## 7. Performance Classification

The system classifies performance based on the calculated percentage:

- 80% and above: Excellent
- 60% to below 80%: Good
- 40% to below 60%: Average
- Below 40%: Needs Improvement

## 8. Technology

The project is developed using:

- Python 3
- JSON for data storage
- Python unittest for testing
- Command-line interface

## 9. Project Objective

The objective of the project is to develop a simple and structured Python application that can assess student skills, analyze performance, store assessment information, and generate useful assessment reports.

## 10. Expected Outcome

The expected outcome is a functional command-line Student Skill Assessment System that provides a structured assessment of student skills and helps identify areas of strength and areas requiring improvement.