from db.run_sql import run_sql
from models.booking import Booking


def new(booking):
    sql = "INSERT INTO bookings ( activity, member ) VALUES ( %s, %s) RETURNING *;"
    values = [ booking.activity.id, booking.member.id ]
    results = run_sql(sql, values)
    booking.id = results[0]["id"]
    return booking

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

def delete_all():
    sql = "DELETE FROM public.bookings"
    run_sql(sql)


def delete_one(id):
    sql = "DELETE  FROM bookings WHERE id = %s"
    value = [id]
    run_sql(sql, value)

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
    run_sql(sql, values)