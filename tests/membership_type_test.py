import unittest

from app.models.membership_type import MembershipType


class TestMembershipType(unittest.TestCase):
    def setUp(self):
        self.premium = MembershipType("Premium")
        self.basic = MembershipType("Basic")

    def test_premium_membership_type(self):
        self.assertEqual("Premium", self.premium.type)

    def test_basic_membership_type(self):
        self.assertEqual("Basic", self.basic.type)