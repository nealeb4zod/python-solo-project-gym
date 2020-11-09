class Activity:
    def __init__(
        self,
        name,
        instructor,
        date_time,
        duration,
        capacity,
        membership_type,
        id = None,
    ):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.date_time = date_time
        self.duration = duration
        self.capacity = capacity
        self.membership_type = membership_type
