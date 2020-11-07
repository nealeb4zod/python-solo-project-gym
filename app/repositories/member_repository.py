from app.db.run_sql import run_sql

from app.models.member import Member

# CREATE member


def add(member):
    sql = "INSERT INTO members( first_name, last_name, date_of_birth, address, phone_number, email, membership_type, start_date, active_membership ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *;"
    values = [
        member.first_name,
        member.last_name,
        member.date_of_birth,
        member.address,
        member.phone_number,
        member.email_address,
        member.membership_type,
        member.start_date,
        member.active_membership,
    ]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


# SELECT all members
def get_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = member(
            row["id"],
            row["first_name"],
            row["last_name"],
            row["address"],
            row["phone_number"],
            row["date_of_birth"],
            row["email"],
            row["membership_type"],
            row["start_date"],
            row["active_membership"]
        )
        members.append(member)
    return members


# SELECT an member
def get_one(id):
    members = []

    sql = "SELECT * FROM members WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        member = member(
            result["id"],
            result["first_name"],
            result["last_name"],
            result["address"],
            result["phone_number"],
            result["date_of_birth"],
            result["email_address"],
            result["membership_type"],
            result["start_date"],
            result["active_membership"]
        )
    return member


# DELETE all members
def delete_all():
    sql = "DELETE FROM public.members"
    results = run_sql(sql)


# DELETE an member
def delete_one(id):
    sql = "DELETE  FROM members WHERE id = %s"
    value = [id]
    results = run_sql(sql, value)


# UPDATE an member
def edit(member):
    sql = "UPDATE members SET (id) = (%s), (first_name = (%s), (last_name) = (%s), (address) = (%s), (phone_number) = (%s), (date_of_birth) = (%s),  (email) = (%s), (membership_type) = (%s), (start_date) = (%s), (active_membership) = (%s);"
    values = [
        member.id,
        member.first_name,
        member.last_name,
        member.address,
        member.phone_number,
        member.date_of_birth,
        member.email_address,
        member.membership_type,
        member.start_date,
        member.active_membership,
    ]
    results = run_sql(sql, values)
