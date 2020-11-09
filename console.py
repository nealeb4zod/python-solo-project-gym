import pdb

from models.instructor import Instructor
from models.member import Member
from models.membership_type import MembershipType
from models.activity import Activity
from models.booking import Booking

import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.membership_type_repository as membership_type_repository
import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

instructor_repository.delete_all()
member_repository.delete_all()
membership_type_repository.delete_all()
activity_repository.delete_all()

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

instructor_repository.new(instructor_1)
instructor_repository.new(instructor_2)


premium = MembershipType("Premium")
basic = MembershipType("Basic")
membership_type_repository.new(premium)
membership_type_repository.new(basic)


member_1 = Member(
    'Kristen',
    'Mahood',
    '1992-03-04',
    '9354 Merry Center',
    '8393426533',
    'kmahood0@bloomberg.com',
    premium,
    '2020-03-03',
    True,
    [],
)
member_2 = Member(
    'Scott',
    'Ponsonby-Smythe',
    '1972-05-29',
    'Great Scott House',
    '1',
    'poshgit@bloomberg.com',
    basic,
    '2020-04-01',
    True,
    [],
)

member_list = []
member_repository.new(member_1)
member_repository.new(member_2)

activity_1 = Activity("Yoga", instructor_2, "2020-11-13 13:00:00", 60, 20, [member_list], premium)
activity_2 = Activity("Pilates", instructor_2, "2020-11-14 12:00:00", 60, 20, [member_list], basic)

activity_repository.new(activity_1)
activity_repository.new(activity_2)

booking_1 = Booking(activity_1, member_1)
booking_repository.new(booking_1)

pdb.set_trace()
