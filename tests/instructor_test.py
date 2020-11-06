import unittest

from app.models.instructor import Instructor
from app.models.activity import Activity
from app.models.member import Member
from app.models.membership_type import MembershipType
from app.models.instructor import Instructor


class TestInstructor(unittest.TestCase):
    def setUp(self):
        self.premium = MembershipType("Premium")
        self.basic = MembershipType("Basic")
        self.member_1 = Member(
            "Paul",
            "Johnston",
            "1999-08-13",
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE",
            "0777666543",
            "alan@emailaddress.com",
            self.premium,
            "2020-05-01",
            True,
        )
        self.member_list = [self.member_1]
        self.instructor_1 = Instructor(
            "Alan",
            "Johnston",
            "1999-08-13",
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE",
            "0777666543",
            [],
        )
        self.activity_1 = Activity(
            "Yoga",
            self.instructor_1,
            "2020-11-13 13:00:00",
            60,
            20,
            [self.member_list],
            self.premium,
        )
        self.activity_2 = Activity(
            "Pilates", self.instructor_1, "2020-11-14 12:00:00", 60, 20, [], self.basic
        )
        self.activity_list = [self.activity_1, self.activity_2]

        self.instructor_2 = Instructor(
            "Scott",
            "Johnston",
            "1999-08-13",
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE",
            "0777666543",
            [self.activity_list],
        )

    def test_instructor_first_name(self):
        self.assertEqual("Alan", self.instructor_1.first_name)

    def test_instructor_last_name(self):
        self.assertEqual("Johnston", self.instructor_1.last_name)

    def test_instructor_date_of_birth(self):
        self.assertEqual("1999-08-13", self.instructor_1.date_of_birth)

    def test_instructor_address(self):
        self.assertEqual(
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE", self.instructor_1.address
        )

    def test_instructor_phone_number(self):
        self.assertEqual("0777666543", self.instructor_1.phone_number)

    def test_instructor_activity_list(self):
        self.assertEqual(2, len(self.instructor_2.list_of_activities[0]))
