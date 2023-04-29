
import pytest

from person_def import Person

def test_PersonInit_WhenAllConditionsAreMet_CreatesObjectPyTest():
    # Arrange
    person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

    # Act
    person.last_name = 'Test'

    # Assert
    assert person.last_name == 'Test'
    assert person.first_name == 'FirstName'
    assert person.school == 'School'

def test_PersonInit_WhenFirstNameIsBlank_CreatesObjectPyTest():
    # Arrange
    person = Person('LastName', '', 'School', 'none', 'none', 'none')

    # Act
    person.last_name = 'Test'

    # Assert
    assert person.first_name == ''

def test_PersonInit_WhenSchoolIsBlank_CreatesObjectPyTest():
    # Arrange
    person = Person('LastName', 'FirstName', '', 'none', 'none', 'none')

    # Act
    person.last_name = 'Test'

    # Assert
    assert person.school == ''