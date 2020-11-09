class Instructor:
    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        address,
        phone_number,
        list_of_activities=None,
        id=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.list_of_activities = list_of_activities
        self.id = id