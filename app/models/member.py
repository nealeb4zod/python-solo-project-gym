class Member:
    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        address,
        phone_number,
        email_address,
        membership_type,
        start_date,
        active_membership,
        activities_booked = None,
        id=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address
        self.membership_type = membership_type
        self.start_date = start_date
        self.active_membership = active_membership
        self.activities_booked = activities_booked
        self.id = id
