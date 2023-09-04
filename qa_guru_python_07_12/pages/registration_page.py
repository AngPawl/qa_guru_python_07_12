from selene import browser, have, command

from qa_guru_python_07_12.resources import resource_path


class RegistrationPage:
    def __init__(self):
        self.google_ad = browser.all('[id^=google_ads][id$=container__]')
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = (
            lambda gender: browser.all('[name=gender]')
            .element_by(have.value(gender.value))
            .element('..')
        )
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth_element = browser.element('#dateOfBirthInput')
        self.date_of_birth_year = (
            lambda year: browser.element('.react-datepicker__year-select')
            .all('option')
            .element_by(have.exact_text(year))
        )
        self.date_of_birth_day = lambda day: browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        )
        self.date_of_birth_month = (
            lambda month: browser.element('.react-datepicker__month-select')
            .all('option')
            .element_by(have.exact_text(month))
        )
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = lambda hobbies: browser.all(
            '[id^=hobbies][type=checkbox]+label'
        ).element_by(have.exact_text(hobbies.value))
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = lambda: browser.element('#submit').perform(command.js.click)
        self.registration_confirmation_popup = browser.element(
            '.modal-header>.modal-title'
        )
        self.registration_confirmation_info_table = (
            browser.element('.table').all('td').even
        )
        self.drop_down_options = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open('/automation-practice-form')

        self.google_ad.with_(timeout=10).wait_until(have.size_greater_than_or_equal(3))
        self.google_ad.perform(command.js.remove)
        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.8)"'
        )

    def register(self, student):
        self.first_name.type(student.first_name)
        self.last_name.type(student.last_name)
        self.user_email.type(student.email)
        self.gender(student.gender).click()
        self.phone_number.type(student.phone_number)
        self.date_of_birth_element.click()
        self.date_of_birth_month(student.date_of_birth.strftime('%B')).click()
        self.date_of_birth_year(student.date_of_birth.strftime('%Y')).click()
        self.date_of_birth_day(student.date_of_birth.strftime('%d')).click()
        self.subjects.type(student.subjects).press_tab()
        self.hobbies(student.hobbies).click()
        self.picture.set_value(resource_path(student.picture_path))
        self.current_address.type(student.address).press_tab()
        self.state.click()
        self.drop_down_options.element_by(have.exact_text(student.state)).click()
        self.city.click()
        self.drop_down_options.element_by(have.exact_text(student.city)).click()
        self.submit()

    def student_should_be_registered(self, student):
        self.registration_confirmation_popup.should(
            have.text('Thanks for submitting the form')
        )
        self.registration_confirmation_info_table.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.email,
                student.gender.value,
                student.phone_number,
                f"{student.date_of_birth.strftime('%d')} {student.date_of_birth.strftime('%B')},{student.date_of_birth.strftime('%Y')}",
                student.subjects,
                student.hobbies.value,
                student.picture_path,
                student.address,
                f'{student.state} {student.city}',
            )
        )
