from db.run_sql import run_sql

from models.booking import Booking

# CREATE booking


def new(booking):
    sql = "INSERT INTO bookings ( activity, member ) VALUES ( %s, %s) RETURNING *;"
    values = [ booking.activity.id, booking.member.id ]
    results = run_sql(sql, values)
    booking.id = results[0]["id"]
    return booking


# SELECT all bookings
def get_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        booking = Booking(
            row["activity"],
            row["member"],
            row["id"],
        )
        bookings.append(booking)
    return bookings


# SELECT an booking
def get_one(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        booking = Booking(
            result["activity"],
            result["member"],
            result["id"],
        )
    return booking


# DELETE all bookings
def delete_all():
    sql = "DELETE FROM public.bookings"
    results = run_sql(sql)


# DELETE an booking
def delete_one(id):
    sql = "DELETE  FROM bookings WHERE id = %s"
    value = [id]
    results = run_sql(sql, value)


def check_booking_exists(activity, member):
    sql = "SELECT * FROM bookings WHERE activity = %s AND member = %s"
    values = [activity, member]
    results = run_sql(sql, values)
    if len(results) == 0:
        return False
    else:
        return True

def delete_specific_booking(member, activity):
    sql = "DELETE  FROM bookings WHERE member = %s and activity = %s"
    values = [member, activity]
    results = run_sql(sql, values)