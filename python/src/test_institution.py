
import pytest

from person_def import Person
from institution_def import Institution
from course_def import Course
from course_offering_def import CourseOffering
from student_def import Student
from instructor_def import Instructor

def test_VerifyRegisterStudenForCourse_WhenAllConditionsMet():

    
    # Arrange
    # Define a course and a course offering
    #
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    faculty = "Professor"
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)


    # Define a student
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")

    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)

    # Enroll the student into the school
    institution.enroll_student(student1)
    

    courseSchedule = institution.course_schedule
    # Act
    # Register the student for the course
    institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

    # Assert
    assert len(courseOffering.registered_students) == 1
    #Is the student enrolled in the institution?
    assert len(institution.student_list) == 1
    #Is the course added to the course catalog?
    assert len(institution.course_catalog) == 1
   


def test_VerifyAssignProfessorForCourse_WhenAllConditionsMet():

    
    # Arrange
    # Define a course and a course offering
    #
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    faculty = "Professor"
    instructor = Instructor("Inst", "Inst", "School Test", "4/20/2023", "inst")
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)



    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)

    courseSchedule = institution.course_schedule
    # Act
    # Hire professor to institution
    institution.hire_instructor(instructor)
    institution.assign_instructor(instructor, courseName, department, "1234", "123","2023", "1")

    # Assert
    #Is the course added to the course catalog?
    assert len(institution.course_catalog) == 1
    assert len(institution.faculty_list) == 1

def test_VerifyAssignProfessorForCourse_WhenHireConditionsNotMet():

    
    # Arrange
    # Define a course and a course offering
    #
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    faculty = "Professor"
    instructor = Instructor("Inst", "Inst", "School Test", "4/20/2023", "inst")
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)



    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)

    courseSchedule = institution.course_schedule
    # Act
    # Hire professor to institution
    #institution.hire_instructor(instructor)
    institution.assign_instructor(instructor, courseName, department, "1234", "123","2023", "1")

    # Assert
    #Is the course added to the course catalog?
    assert len(institution.course_catalog) == 1
    assert len(institution.faculty_list) == 0

def test_VerifyRegisterStudenForCourse_WhenStudentConditionNotMet():

    
    # Arrange
    # Define a course and a course offering
    #
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)

    # Define a student
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")

    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)

    # Enroll the student into the school
    institution.enroll_student(student1)

    courseSchedule = institution.course_schedule
    # Act
    # Register the student for the course
    institution.register_student_for_course("noOne", courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

    # Assert
    #Is the student registered for the course?
    assert len(courseOffering.registered_students) == 0
    #Is the student enrolled in the institution?
    assert len(institution.student_list) == 1
    #Is the course added to the course catalog?
    assert len(institution.course_catalog) == 1



def test_VerifyRegisterMultipleStudentsForCourse_WhenAllConditionsMet():

    
    # Arrange
    # Define a course and a course offering
    #
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)

    # Define a student
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")
    student2 = Student("Test1", "Test1", "School Test1", "4/21/2023", "test1")

    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)

    # Enroll the student into the school
    institution.enroll_student(student1)
    institution.enroll_student(student2)


    courseSchedule = institution.course_schedule
    # Act
    # Register the student for the course
    institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)
    institution.register_student_for_course(student2, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

    # Assert
    assert len(courseOffering.registered_students) > 1
    #Is there more than 1 student enrolled in the institution?
    assert len(institution.student_list) > 1
    #Is there 1 course added to the course catalog?
    assert len(institution.course_catalog) == 1


def test_VerifyRegisterMultipleStudentsForMultipleCourse_WhenAllConditionsMet():

    
    # Arrange
    # Define a course and a course offering
    #
    department = "ComputerScience"
    courseNumber = 1234
    courseName = "TestClass"
    courseNumber1 = 1334
    courseName1 = "TestClass1"
    courseCredits = 3
    courseSectionNumber = 123
    courseOfferYear = 2023
    courseQuarter = 1
    course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
    course1 = Course(department=department, number=courseNumber1, name=courseName1, credits= courseCredits)
    courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)
    courseOffering1 = CourseOffering(course1, courseSectionNumber, courseOfferYear, courseQuarter)

    # Define a student
    student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")
    student2 = Student("Test1", "Test1", "School Test1", "4/21/2023", "test1")
    student3 = Student("Test2", "Test2", "School Test2", "4/20/2023", "test2")
    student4 = Student("Test3", "Test3", "School Test3", "4/21/2023", "test13")

    # Define an institution
    institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
    institution.add_course(course)
    institution.add_course(course1)

    # Add the course to to the planned course offerings
    institution.add_course_offering(courseOffering)
    institution.add_course_offering(courseOffering1)

    # Enroll the student into the school
    institution.enroll_student(student1)
    institution.enroll_student(student2)
    institution.enroll_student(student3)
    institution.enroll_student(student4)


    courseSchedule = institution.course_schedule
    # Act
    # Register the student for the course
    institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)
    institution.register_student_for_course(student2, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)
    institution.register_student_for_course(student3, courseName1, department, courseNumber1, courseSectionNumber, courseOfferYear, courseQuarter)
    institution.register_student_for_course(student4, courseName1, department, courseNumber1, courseSectionNumber, courseOfferYear, courseQuarter)

    # Assert
    assert len(courseOffering.registered_students) > 1
    assert len(courseOffering1.registered_students) > 1
    #Is there more than 1 student enrolled in the institution?
    assert len(institution.student_list) == 4
    #Is there 1 course added to the course catalog?
    assert len(institution.course_catalog) == 2




def test_Verify_CourseSchedule_WhenAllConditionsMet():

        # Arrange
        # Need Institution
        institution = Institution("Quinnipiac University", "qu.edu")
        course = Course("Computer Science", 1234, "Test Class", 3)
        course1 = Course("Biology", 1234, "Test Class1", 3)
        courseOffering1 = CourseOffering(course, "123", "2023", "1")
        courseOffering2 = CourseOffering(course, "123", "2023", "2")
        courseOffering3 = CourseOffering(course1, "123", "2023", "1")
        courseOffering4 = CourseOffering(course1, "123", "2023", "2")
        
        compSciOfferingList = [courseOffering1, courseOffering2]
        bioOfferingList = [courseOffering3, courseOffering4]
        courseScheduleList = [compSciOfferingList, bioOfferingList]
        institution.course_schedule = courseScheduleList

        # Act
       
        # Assert
        assert len(institution.course_schedule) == 2

