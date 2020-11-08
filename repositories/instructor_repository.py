from db.run_sql import run_sql

from models.instructor import Instructor
from models.activity import Activity

# CREATE instructor

def get_activities(instructor_id):
    activities = []

    sql = "SELECT * FROM activities WHERE instructor = %s"
    value = [instructor_id]
    results = run_sql(sql, value)

    for row in results:
        activity = Activity(
            row["name"],
            row["instructor"],
            row["date_time"],
            row["duration"],
            row["capacity"],
            row["membership_type"],
            row["id"],
        )
        activities.append(activity)
    return activities


def new(instructor):
    sql = "INSERT INTO instructors( first_name, last_name, date_of_birth, address, phone_number ) VALUES ( %s, %s, %s, %s, %s ) RETURNING *;"
    values = [
        instructor.first_name,
        instructor.last_name,
        instructor.date_of_birth,
        instructor.address,
        instructor.phone_number,
    ]
    results = run_sql(sql, values)
    instructor.id = results[0]["id"]
    return instructor


# SELECT all instructors
def get_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)

    for row in results:
        list_of_activities = get_activities(row["id"],)
        instructor = Instructor(
            row["first_name"],
            row["last_name"],
            row["date_of_birth"],
            row["address"],
            row["phone_number"],
            list_of_activities,
            row["id"],
        )
        instructors.append(instructor)
    return instructors


# SELECT an instructor
def get_one(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    list_of_activities = get_activities(id)
    if result is not None:
        instructor = Instructor(
            result["first_name"],
            result["last_name"],
            result["date_of_birth"],
            result["address"],
            result["phone_number"],
            list_of_activities,
            result["id"],
        )
    return instructor


# DELETE all instructors
def delete_all():
    sql = "DELETE FROM public.instructors"
    results = run_sql(sql)


# DELETE an instructor
def delete_one(id):
    sql = "DELETE  FROM instructors WHERE id = %s"
    value = [id]
    results = run_sql(sql, value)


# UPDATE an instructor
def edit(instructor):
    sql = "UPDATE instructors SET  (first_name = (%s), (last_name) = (%s), (address) = (%s), (phone_number) = (%s), (date_of_birth) = (%s) WHERE id = %s;"
    values = [
        instructor.first_name,
        instructor.last_name,
        instructor.address,
        instructor.phone_number,
        instructor.date_of_birth,
        instructor.id,
    ]
    results = run_sql(sql, values)
