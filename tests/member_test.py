import unittest

from models.member import Member
from models.membership_type import MembershipType
from models.activity import Activity
from models.instructor import Instructor


class TestMember(unittest.TestCase):
    def setUp(self):
        self.premium = MembershipType("Premium")
        self.instructor_1 = Instructor(
            "Alan",
            "Johnston",
            "1999-08-13",
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE",
            "0777666543",
        )
        self.activity_1 = Activity(
            "Yoga",
            self.instructor_1,
            "2020-11-13 13:00:00",
            60,
            20,
            self.premium,
            True,
        )
        self.activity_2 = Activity(
            "Pilates", self.instructor_1, "2020-11-14 12:00:00", 60, 20, self.premium, True,
        )
        activities_list = [self.activity_1, self.activity_2]
        self.member_1 = Member(
            "Alan",
            "Johnston",
            "1999-08-13",
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE",
            "0777666543",
            "alan@emailaddress.com",
            self.premium,
            "2020-05-01",
            True,
        )

    def test_member_first_name(self):
        self.assertEqual("Alan", self.member_1.first_name)

    def test_member_last_name(self):
        self.assertEqual("Johnston", self.member_1.last_name)

    def test_member_date_of_birth(self):
        self.assertEqual("1999-08-13", self.member_1.date_of_birth)

    def test_member_address(self):
        self.assertEqual(
            "59 Avenue Avenue, Cowdenbeath, KY7 0GE", self.member_1.address
        )

    def test_member_phone_number(self):
        self.assertEqual("0777666543", self.member_1.phone_number)

    def test_member_email_address(self):
        self.assertEqual("alan@emailaddress.com", self.member_1.email_address)

    def test_member_membership_type(self):
        self.assertEqual(self.premium, self.member_1.membership_type)

    def test_member_start_date(self):
        self.assertEqual("2020-05-01", self.member_1.start_date)

    def test_member_active_membership(self):
        self.assertEqual(True, self.member_1.active_membership)
