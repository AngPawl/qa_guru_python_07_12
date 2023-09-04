import dataclasses
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: date
    subjects: str
    hobbies: Hobbies
    picture_path: str
    address: str
    state: str
    city: str


student = User(
    first_name='John',
    last_name='Doe',
    email='test_email.demoqa@test.com',
    gender=Gender.male,
    phone_number='8800111111',
    date_of_birth=date(2000, 1, 1),
    subjects='Computer Science',
    hobbies=Hobbies.sports,
    picture_path='student.png',
    address='42 Best street, suite 1, Dallas, TX, 11111',
    state='NCR',
    city='Delhi',
)
