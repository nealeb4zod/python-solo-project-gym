class Activity:
    def __init__(
        self,
        name,
        instructor,
        date_time,
        duration,
        capacity,
        list_of_members,
        membership_type,
        id = None,
    ):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.date_time = date_time
        self.duration = duration
        self.capacity = capacity
        self.list_of_members = list_of_members
        self.membership_type = membership_type
