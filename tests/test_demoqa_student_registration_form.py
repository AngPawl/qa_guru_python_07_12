from qa_guru_python_07_12.data import users
from qa_guru_python_07_12.pages.registration_page import RegistrationPage


def test_successful_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # When
    registration_page.register(users.student)

    # Then
    registration_page.student_should_be_registered(users.student)
