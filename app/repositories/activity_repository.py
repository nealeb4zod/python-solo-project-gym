from app.db.run_sql import run_sql

from app.models.activity import Activity

# CREATE activity


def add(activity):
    sql = "INSERT INTO activities( name, instructor, date_time, duration, capacity, membership_type ) VALUES ( %s, %s, %s, %s, %s, %s) RETURNING *;"
    values = [
        activity.name,
        activity.instructor,
        activity.date_time,
        activity.duration,
        activity.capacity,
        activity.membership_type,
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
        activity = Activity(
            result["name"],
            result["instructor"],
            result["date_time"],
            result["duration"],
            result["capacity"],
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
    sql = "UPDATE activities SET ((name) = (%s), (instructor) = (%s), (date_time) = (%s), (duration) = (%s), (capacity) = (%s),  (membership_type) = (%s) WHERE id = %s;"
    values = [
        activity.name,
        activity.instructor,
        activity.date_time,
        activity.duration,
        activity.capacity,
        activity.membership_type,
        activity.id,
    ]
    results = run_sql(sql, values)
