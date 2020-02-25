#Payton Boekhout
#plb4dq
#PyTest Assignment 5

import json
import pytest
import Professor
import Student
import System
import TA
import random
import string

student = 'akend3'
course = 'databases'
assignment = 'assignment1'
user = 'goggins'
password = 'augurrox'

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
    st = Student.Student(student, users, courses)
    st.submit_assignment('databases', 'assignment1', 'blah blah blah', '01/21/2021')

    for key in users:
        if '01/21/2021' in users['akend3']['courses']['databases']['assignment1']['submission_date']:
            assert True
        else:
            assert False


def test_check_ontime(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    st = Student.Student(student, users, courses)

    if st.check_ontime('02/04/2021', '02/03/2021'):
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
    st = Student.Student('akend3', users, courses)
    grades = st.view_assignments('databases')
    if grades[0][1] == '1/14/20':
        assert True
    else:
        assert False


#These are the tests that I made

# This test checks to see if different proffesors can change grades of the
# classes they dont teach
def test_proffesor_change(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    prof = Professor.Professor('goggins', users, courses)
    prof.change_grade(student,course, assignment, 100)

    for key in users:
        if users[student]['courses'][course][assignment]['grade'] == 0:
            assert False
        else:
            assert True

            
# This test checks to see if a proffesor not teaching a a certain class can
# create an assignment for it
def test_wrong_create(grading_system):
    grading_system.login(user, password)
    grading_system.usr.create_assignment('assignment5', '02/28/20', 'cloud_computing')
    grading_system.reload_data()
    grading_system.login('hdjsr7', 'pass1234')
    
    assignments = grading_system.usr.view_assignments('cloud_computing')
    assert 'assignment5' in assignments


# This test checks to see if a proffesor not teaching a class can drop a student
# from that course
def test_wrong_drop(grading_system):
    grading_system.login(user, password)
    grading_system.usr.drop_student(student, 'comp_sci')
    grading_system.reload_data()
    grading_system.login(student, '123454321')
    
    courses = grading_system.usr.courses
    assert 'comp_sci' in courses


# This test checks to see if a TA change change the grade of students not
# in their class
def test_TA_change(grading_system):
    users = grading_system.users
    person = TA.TA('cmhbf5',users,course)
    person.change_grade(student,course,assignment,100)

    for key in users:
       if users[student]['courses'][course][assignment]['grade'] == 0:
           assert False
       else:
           assert True


# This test checks to see if a proffesor of a class they dont teach can check
# those grades
def test_wrong_check(grading_system):
    grading_system.login(username, password)
    grades = grading_system.usr.check_grades(student, 'comp_sci')
    assert grades == []


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
