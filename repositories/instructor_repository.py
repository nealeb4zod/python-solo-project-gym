from db.run_sql import run_sql

from models.instructor import Instructor
from models.activity import Activity


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
            row["active"],
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

def get_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)

    for row in results:
        instructor = Instructor(
            row["first_name"],
            row["last_name"],
            row["date_of_birth"],
            row["address"],
            row["phone_number"],
            row["id"],
        )
        instructors.append(instructor)
    return instructors

def get_one(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        instructor = Instructor(
            result["first_name"],
            result["last_name"],
            result["date_of_birth"],
            result["address"],
            result["phone_number"],
            result["id"],
        )
    return instructor

def delete_all():
    sql = "DELETE FROM public.instructors"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE  FROM instructors WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def edit(instructor):
    sql = "UPDATE instructors SET  (first_name, last_name, address, phone_number, date_of_birth) = (%s, %s, %s, %s, %s) WHERE id = %s;"
    values = [
        instructor.first_name,
        instructor.last_name,
        instructor.address,
        instructor.phone_number,
        instructor.date_of_birth,
        instructor.id,
    ]
    run_sql(sql, values)
