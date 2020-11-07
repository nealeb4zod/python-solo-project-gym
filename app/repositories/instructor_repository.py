from app.db.run_sql import run_sql

from app.models.instructor import Instructor

# CREATE instructor


def add(instructor):
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
        instructor = Instructor(
            row["first_name"],
            row["last_name"],
            row["address"],
            row["phone_number"],
            row["date_of_birth"],
            row["id"],
        )
        instructors.append(instructor)
    return instructors


# SELECT an instructor
def get_one(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        instructor = Instructor(
            result["first_name"],
            result["last_name"],
            result["address"],
            result["phone_number"],
            result["date_of_birth"],
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
