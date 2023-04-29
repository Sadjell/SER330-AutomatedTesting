
import pytest

from student_def import Student


def test_StudentInit_WhenAllConditionsAreMet_CreatesObjectPyTest():
    # Arrange
    student = Student('LastName', 'FirstName', 'School', '01/06/1999', 'username')
    department = "ComputerScience"
    
    

    # Assert
    assert student.last_name == 'LastName'
    assert student.first_name == 'FirstName'
    assert student.school == 'School'
    assert student.credits == 0
    assert student.gpa == 0.0

def test_StudentInit_WhenFirstNameIsBlank_CreatesObjectPyTest():
    # Arrange
    student = Student('LastName', '', 'School', '01/06/1999', 'username')

    # Act
    student.last_name = 'Test'

    # Assert
    assert student.first_name == ''

def test_StudentInit_WhenSchoolIsBlank_CreatesObjectPyTest():
    # Arrange
    student = Student('LastName', 'FirstName', '', '01/06/1999', 'username')

    # Act
    student.last_name = 'Test'

    # Assert
    assert student.school == ''

