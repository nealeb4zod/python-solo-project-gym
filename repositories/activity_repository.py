from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member
import repositories.member_repository as member_repository


def get_members(id):
    members = []

    sql = "SELECT * FROM members INNER JOIN bookings ON members.id = bookings.member WHERE bookings.activity = %s"
    value = [id]
    results = run_sql(sql, value)

    for row in results:
        activities_booked = member_repository.get_activities(row["id"])
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
            activities_booked,
            row["id"]
        )
        members.append(member)
    return members


# CREATE activity
def new(activity):
    sql = "INSERT INTO activities( name, instructor, date_time, duration, capacity, membership_type ) VALUES ( %s, %s, %s, %s, %s, %s) RETURNING *;"
    values = [
        activity.name,
        activity.instructor.id,
        activity.date_time,
        activity.duration,
        activity.capacity,
        activity.membership_type.id,
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
        list_of_members = get_members(row["id"])
        activity = Activity(
            row["name"],
            row["instructor"],
            row["date_time"],
            row["duration"],
            row["capacity"],
            list_of_members,
            row["membership_type"],
            row["id"],
        )
        activities.append(activity)
    return activities


# SELECT an activity
def get_one(id):
    sql = "SELECT * FROM activities WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        list_of_members = get_members(result["id"])
        activity = Activity(
            result["name"],
            result["instructor"],
            result["date_time"],
            result["duration"],
            result["capacity"],
            list_of_members,
            result["membership_type"],
            result["id"],
        )
    return activity


# DELETE all activities
def delete_all():
    sql = "DELETE FROM public.activities"
    results = run_sql(sql)


# DELETE an activity
def delete_one(id):
    sql = "DELETE  FROM activities WHERE id = %s"
    value = [id]
    results = run_sql(sql, value)


# UPDATE an activity
def edit(activity):
    sql = "UPDATE activities SET (name, instructor, date_time, duration, capacity, membership_type) = (%s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [
        activity.name,
        activity.instructor.id,
        activity.date_time,
        activity.duration,
        activity.capacity,
        activity.membership_type.id,
        activity.id,
    ]
    results = run_sql(sql, values)
