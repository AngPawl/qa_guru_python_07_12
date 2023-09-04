import os
from selene import browser, command, have
import tests


def test_successful_student_registration_form():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
    browser.execute_script(
        'document.querySelector(".body-height").style.transform = "scale(.8)"'
    )

    # When
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test_email.demoqa@test.com')

    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    browser.element('#userNumber').type('8800111111')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').all('option').element_by(
        have.exact_text('January')
    ).click()

    browser.element('.react-datepicker__year-select').all('option').element_by(
        have.exact_text('2000')
    ).click()
    browser.element(
        f'.react-datepicker__day--00{1}:not(.react-datepicker__day--outside-month)'
    ).click()

    browser.element('#subjectsInput').type('computer').press_tab()

    browser.all('[id^=hobbies][type=checkbox]+label').element_by(
        have.exact_text('Sports')
    ).click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/student.png')
        )
    )

    browser.element('#currentAddress').type(
        '42 Best street, suite 1, Dallas, TX, 11111'
    ).press_tab()

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('#submit').perform(command.js.click)

    # Then
    browser.element('.modal-header>.modal-title').should(
        have.text('Thanks for submitting the form')
    )

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'John Doe',
            'test_email.demoqa@test.com',
            'Male',
            '8800111111',
            '01 January,2000',
            'Computer Science',
            'Sports',
            'student.png',
            '42 Best street, suite 1, Dallas, TX, 11111',
            'NCR Delhi',
        )
    )
