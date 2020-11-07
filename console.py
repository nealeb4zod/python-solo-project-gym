import pdb

from app.models.instructor import Instructor

import app.repositories.instructor_repository as instructor_repository

instructor_repository.delete_all()

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
pdb.set_trace()
