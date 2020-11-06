import unittest

from app.models.activity import Activity
from app.models.member import Member
from app.models.membership_type import MembershipType
from app.models.instructor import Instructor


class TestActivity(unittest.TestCase):
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

    def test_activity_has_name(self):
        self.assertEqual("Yoga", self.activity_1.name)

    def test_activity_has_instructor(self):
        self.assertEqual(self.instructor_1, self.activity_1.instructor)

    def test_activity_has_datetime(self):
        self.assertEqual("2020-11-13 13:00:00", self.activity_1.date_time)

    def test_activity_has_duration(self):
        self.assertEqual(60, self.activity_1.duration)

    def test_activity_has_capacity(self):
        self.assertEqual(20, self.activity_1.capacity)

    def test_activity_has_list_of_members(self):
        self.assertEqual(1, len(self.activity_1.list_of_members))

    def test_activity_has_membership_type(self):
        self.assertEqual("Premium", self.activity_1.membership_type.type)
