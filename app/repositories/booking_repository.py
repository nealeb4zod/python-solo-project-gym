from app.db.run_sql import run_sql

from app.models.bookin import Booking

# CREATE booking


def add(booking):
    sql = "INSERT INTO bookings ( activity, member ) VALUES ( %s, %s) RETURNING *;"
    values = [ booking.activity, booking.member ]
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


# UPDATE an booking
def edit(booking):
    sql = "UPDATE bookings SET (activity, member) = (%s, %s) WHERE id = %s;"
    values = [
        booking.activity,
        booking.member,
        booking.id,
    ]
    results = run_sql(sql, values)
