from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity


def get_activities(user_id):
    activities = []

    sql = "SELECT activities.* FROM activities INNER JOIN bookings on activities.id = bookings.activity where bookings.member = %s"
    value = [user_id]
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

def new(member):
    sql = "INSERT INTO members( first_name, last_name, date_of_birth, address, phone_number, email_address, membership_type, start_date, active_membership ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *;"
    values = [
        member.first_name,
        member.last_name,
        member.date_of_birth,
        member.address,
        member.phone_number,
        member.email_address,
        member.membership_type.id,
        member.start_date,
        member.active_membership,
    ]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member

def get_all():
    members = []

    sql = "SELECT * FROM members ORDER BY last_name ASC"
    results = run_sql(sql)

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

def get_all_active():
    members = []

    sql = "SELECT * FROM members where active_membership = true ORDER BY last_name ASC"
    results = run_sql(sql)

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
def get_all_inactive():
    members = []

    sql = "SELECT * FROM members where active_membership = false ORDER BY last_name ASC"
    results = run_sql(sql)

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

def get_one(id):
    sql = "SELECT * FROM members WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        member = Member(
            result["first_name"],
            result["last_name"],
            result["date_of_birth"],
            result["address"],
            result["phone_number"],
            result["email_address"],
            result["membership_type"],
            result["start_date"],
            result["active_membership"],
            result["id"],
        )
    return member

def delete_all():
    sql = "DELETE FROM public.members"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE  FROM members WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def edit(member):
    sql = "UPDATE members SET (first_name, last_name, date_of_birth, address, phone_number, email_address, membership_type, start_date, active_membership) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [
        member.first_name,
        member.last_name,
        member.date_of_birth,
        member.address,
        member.phone_number,
        member.email_address,
        member.membership_type.id,
        member.start_date,
        member.active_membership,
        member.id,
    ]
    run_sql(sql, values)
