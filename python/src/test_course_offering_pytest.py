
import pytest

from course_offering_def import CourseOffering
from course_def import Course
from student_def import Student
from institution_def import Institution

# Example of test cases using the Pytest Framework 
# There is no class in this case. 
# Test Methods can exist outside of a class

def test_VerifyGradeSubmission_WhenAllConditionsAreMet_ReturnsTrue_Pytest():
    
    # Arrange
    course = Course("Computer Science", 1234, "Test Class", 3)
    cc = CourseOffering(course, "123", "2023", "1")
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
    studentsList = [student1]
    

    # Act
    #cc.register_students(studentsList)
    cc.submit_grade(student1, 'B')

    # Assert
    # Grades is a dictionary not a list
    # Grades are stored in the dictionary by user name
    # Given this we can test for multiple conditions

     # does 1 and only 1 grade exist?
    assert len(cc.grades) == 1
    
    # Is the key of the grade the username for student 1?
    assert cc.grades.keys().__contains__("userName")
    
    #s  Ithe value of this grade a B?
    assert cc.grades.get("userName") == 'B'

def test_VerifyGradeSubmission_WhenGradeConditionIsNotMet_ReturnsNoGrade_Pytest():
    
    # Arrange
    course = Course("Computer Science", 1234, "Test Class", 3)
    cc = CourseOffering(course, "123", "2023", "1")
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
    studentsList = [student1]
    

    # Act
    #cc.register_students(studentsList)
    cc.submit_grade(student1, 0)

    # Assert
    # Grades is a dictionary not a list
    # Grades are stored in the dictionary by user name
    # Given this we can test for multiple conditions

    # was the grade submitted?
    assert len(cc.grades) == 0

def test_VerifyGradeSubmission_WhenMoreThanOneGradeIsSubmitted_Returns_Pytest():
    
    # Arrange
    course = Course("Computer Science", 1234, "Test Class", 3)
    cc = CourseOffering(course, "123", "2023", "1")
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
    studentsList = [student1]
    student2 = Student("Test1", "Test2", "School Test1", "4/20/2023", "userName1")
    

    # Act
    #cc.register_students(studentsList)
    cc.submit_grade(student1, 'B')
    cc.submit_grade(student2, 'B')

    # Assert
    # Grades is a dictionary not a list
    # Grades are stored in the dictionary by user name
    # Given this we can test for multiple conditions

    # do more than one grade exists?
    assert len(cc.grades) > 1

def test_VerifyGradeSubmission_WhenNameConditionIsNotMet_ReturnsNoGrade_Pytest():
    
    # Arrange
    course = Course("Computer Science", 1234, "Test Class", 3)
    cc = CourseOffering(course, "123", "2023", "1")
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "userName")
    studentsList = [student1]
    

    # Act
    #cc.register_students(studentsList)
    cc.submit_grade("noOne", 'B')

    # Assert
    # Grades is a dictionary not a list
    # Grades are stored in the dictionary by user name
    # Given this we can test for multiple conditions

    # was the grade submitted?
    assert len(cc.grades) == 0
    
    


 