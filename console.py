import pdb

from app.models.instructor import Instructor
from app.models.member import Member

import app.repositories.instructor_repository as instructor_repository
import app.repositories.member_repository as member_repository

instructor_repository.delete_all()
member_repository.delete_all()

instructor_1 = Instructor(
    'Alan',
    'Johnston',
    '1999-08-13',
    '59 Avenue Avenue, Cowdenbeath, KY7 0GE',
    '0777666543',
    [],
)

instructor_2 = Instructor(
    'Joey',
    'Muscles',
    '1972-04-26',
    '59 Street Road, Borughty Ferry, DD7 1TY',
    '0777666999',
    [],
)

instructor_repository.add(instructor_1)
instructor_repository.add(instructor_2)
instructor_repository.get_all()
instructor_repository.get_one(instructor_2.id)
instructor_repository.delete_one(instructor_1.id)
instructor_repository.get_all()

member_1 = Member(
    'Kristen',
    'Mahood',
    '1992-03-04',
    '9354 Merry Center',
    '8393426533',
    'kmahood0@bloomberg.com',
    'Basic',
    '2020-03-03',
    True,
)
member_2 = Member(
    'Scott',
    'Ponsonby-Smythe',
    '1972-05-29',
    'Great Scott House',
    '1',
    'poshgit@bloomberg.com',
    'Premium',
    '2020-04-01',
    True,
)

member_repository.add(member_1)
member_repository.add(member_2)
member_repository.get_all()
member_repository.get_one(member_2.id)
member_repository.delete_one(member_1.id)
member_repository.get_all()

pdb.set_trace()
