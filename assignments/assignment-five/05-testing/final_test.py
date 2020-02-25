import json
import pytest
import Professor
import Student
import System
import TA
import random
import string

student = 'akend3'
assignment = 'assignment1'
user = 'goggins'
password = 'augurrox'
course = 'databases'


def test_login(grading_system):
    users = grading_system.users
    grading_system.login(user, password)
    if users[user]['role'] == 'professor':
       assert True


def test_password(grading_system):
    users = grading_system.users
    letter = string.ascii_letters
    testpass = ''.join(random.choice(letter) for i in range(8))
    grading_system.check_password(user,testpass)
    if testpass == users[user]['password']:
          if grading_system.check_password(user,password):
              assert True



def test_change_grade(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor(user, users, courses)
    prof.change_grade(student, course, assignment, 100)

    for key in users:
       if users[student]['courses'][course][assignment]['grade'] == 0:
           assert False
       else:
           assert True



def test_create_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor(user, users, courses)
    prof.create_assignment('assignment3', '01/21/2021', 'databases')

    assignments = []
    for key in courses:
            assignments.append([key, courses[key]])

    if assignments[1][1]['assignments']['assignment3']:
        assert True
    else:
        assert False

def test_add_Student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor(user, users, courses)
    prof.add_student('aden3', 'comp_sci')

    for key in users:
        if key == 'aden3':
            assert True
        else:
            assert False

def test_drop_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor(user, users, courses)
    prof.drop_student(student, 'comp_sci')

    if 'comp_sci' in users[student]['courses']:
        assert False
    else:
        assert True



def test_submit_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    stu = Student.Student(student, users, courses)
    stu.submit_assignment('databases', 'assignment1', 'blah blah blah', '01/21/2021')

    for key in users:
        if '01/21/2021' in users['akend3']['courses']['databases']['assignment1']['submission_date']:
            assert True
        else:
            assert False




def test_check_ontime(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    stu = Student.Student(student, users, courses)

    if stu.check_ontime('02/04/2021', '02/03/2021'):
        assert False
    else:
        assert True



def test_check_grades(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    test = Student.Student(student, users, courses)
    grades = test.check_grades(course)

    if grades[0][1] == 57:
        assert True
    else:
        assert False



def test_view_assignments(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    stu = Student.Student('akend3', users, courses)
    grades = stu.view_assignments('databases')
    if grades[0][1] == '1/5/20':
        assert True
    else:
        assert False


#Tests if a TA can change the grades of a student not in their class
def test_TAGrade(grading_system):
    users = grading_system.users
    taperson = TA.TA('cmhbf5',users,course)
    taperson.change_grade(student,course,assignment,100)

    for key in users:
       if users[student]['courses'][course][assignment]['grade'] == 0:
           assert False
       else:
           assert True

# Tests the ability of a different professor than the one assigned to the class can change class grades
def test_profAccess(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor('goggins', users, courses)
    prof.change_grade(student,course, assignment, 100)

    for key in users:
        if users[student]['courses'][course][assignment]['grade'] == 0:
            assert False
        else:
            assert True

def test_ta(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    ta = TA.TA(user, users, courses)
    ta.create_assignment('assignment4', '01/21/2021', 'databases')

    assignments = []
    for key in courses:
            assignments.append([key, courses[key]])

    if assignments[1][1]['assignments']['assignment4']:
        assert False
    else:
        assert True

def test_profCheck(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor(user, users, courses)
    grades = prof.check_grades(student, course)

    if grades[1][1] == 23:
        assert True
    else:
        assert False

def test_tacheckGrades(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    ta = TA.TA(user, users, courses)
    grades = ta.check_grades(student, course)

    if grades[1][1] == 23:
        assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
