from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member



def get_members(id):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.member WHERE bookings.activity = %s"
    value = [id]
    results = run_sql(sql, value)

    for row in results:
        member = Member(
            row["first_name"],
            row["last_name"],
            row["date_of_birth"],
            row["address"],
            row["phone_number"],
            row["email_address"],
            row["membership_type"],
            row["start_date"],
            row["active_membership"],
            row["id"]
        )
        members.append(member)
    return members


# CREATE activity
def new(activity):
    sql = "INSERT INTO activities( name, instructor, date_time, duration, capacity, membership_type, active ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;"
    values = [
        activity.name,
        activity.instructor.id,
        activity.date_time,
        activity.duration,
        activity.capacity,
        activity.membership_type.id,
        activity.active,
    ]
    results = run_sql(sql, values)
    activity.id = results[0]["id"]
    return activity


# SELECT all activities
def get_all():
    activities = []

    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for row in results:
        activity = Activity(
            row["name"],
            row["instructor"],
            row["date_time"],
            row["duration"],
            row["capacity"],
            row["membership_type"],
            row["active"],
            row["id"],
        )
        activities.append(activity)
    return activities

def get_all_active():
    activities = []

    sql = "SELECT * FROM activities WHERE active = true"
    results = run_sql(sql)

    for row in results:
        activity = Activity(
            row["name"],
            row["instructor"],
            row["date_time"],
            row["duration"],
            row["capacity"],
            row["membership_type"],
            row["active"],
            row["id"],
        )
        activities.append(activity)
    return activities

def get_all_inactive():
    activities = []

    sql = "SELECT * FROM activities WHERE active = false"
    results = run_sql(sql)

    for row in results:
        activity = Activity(
            row["name"],
            row["instructor"],
            row["date_time"],
            row["duration"],
            row["capacity"],
            row["membership_type"],
            row["active"],
            row["id"],
        )
        activities.append(activity)
    return activities


# SELECT an activity
def get_one(id):
    sql = "SELECT * FROM activities WHERE active = true AND id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        activity = Activity(
            result["name"],
            result["instructor"],
            result["date_time"],
            result["duration"],
            result["capacity"],
            result["membership_type"],
            result["active"],
            result["id"],
        )
    return activity


# DELETE all activities
def delete_all():
    sql = "DELETE FROM public.activities"
    run_sql(sql)


# DELETE an activity
def delete_one(id):
    sql = "DELETE  FROM activities WHERE id = %s"
    value = [id]
    run_sql(sql, value)


# UPDATE an activity
def edit(activity):
    sql = "UPDATE activities SET (name, instructor, date_time, duration, capacity, membership_type, active) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [
        activity.name,
        activity.instructor.id,
        activity.date_time,
        activity.duration,
        activity.capacity,
        activity.membership_type.id,
        activity.active,
        activity.id,
    ]
    run_sql(sql, values)
