from db.run_sql import run_sql

from models.membership_type import MembershipType

# CREATE membership_type


def new(membership_type):
    sql = "INSERT INTO membership_types ( type ) VALUES ( %s ) RETURNING *;"
    values = [
        membership_type.type,
    ]
    results = run_sql(sql, values)
    membership_type.id = results[0]["id"]
    return membership_type


# SELECT all membership_types
def get_all():
    membership_types = []

    sql = "SELECT * FROM membership_types"
    results = run_sql(sql)

    for row in results:
        membership_type = MembershipType(
            row["type"],
            row["id"],
        )
        membership_types.append(membership_type)
    return membership_types


# SELECT an membership_type
def get_one(id):
    sql = "SELECT * FROM membership_types WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        membership_type = MembershipType(
            result["type"],
            result["id"],
        )
    return membership_type


# DELETE all membership_types
def delete_all():
    sql = "DELETE FROM public.membership_types"
    results = run_sql(sql)


# DELETE an membership_type
def delete_one(id):
    sql = "DELETE  FROM membership_types WHERE id = %s"
    value = [id]
    results = run_sql(sql, value)


# UPDATE an membership_type
def edit(membership_type):
    sql = "UPDATE membership_types SET (type) = (%s) WHERE id = %s;"
    values = [
        membership_type.type,
        membership_type.id,
    ]
    results = run_sql(sql, values)
