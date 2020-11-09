from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.booking import Booking

import repositories.booking_repository as booking_repository


bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.get_all()
    return render_template("bookings/index.html", bookings=bookings, title="Bookings")

@bookings_blueprint.route("/bookings/new")
def new_booking():
    bookingship_types = bookingship_type_repository.get_all()
    return render_template("bookings/new.html", bookingship_types=bookingship_types, title="New Booking")

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    email_address = request.form["email_address"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    bookingship_type_id = request.form["bookingship_type"]
    start_date = request.form["start_date"]
    active_bookingship = request.form["active_bookingship"]

    bookingship_type = bookingship_type_repository.get_one(bookingship_type_id)
    new_booking = Booking(first_name, last_name, date_of_birth, address, phone_number, email_address, bookingship_type, start_date, active_bookingship)
    booking_repository.new(new_booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.get_one(id)
    bookingship_types = bookingship_type_repository.get_all()
    return render_template("/bookings/edit.html", booking=booking, bookingship_types=bookingship_types, title="Edit Booking Details")

@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    email_address = request.form["email_address"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    bookingship_type_id = request.form["bookingship_type"]
    start_date = request.form["start_date"]
    active_bookingship = request.form["active_bookingship"]


    bookingship_type = bookingship_type_repository.get_one(bookingship_type_id)
    updated_booking = Booking(first_name, last_name, date_of_birth, address, phone_number, email_address, bookingship_type, start_date, active_bookingship, id)
    booking_repository.edit(updated_booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>")
def show_details(id):
    booking = booking_repository.get_one(id)
    booked_activities = booking_repository.get_activities(id)
    bookingship_type = bookingship_type_repository.get_one(booking.bookingship_type)
    return render_template("/bookings/show.html", booking=booking, bookingship_type=bookingship_type, booked_activities=booked_activities, title="Booking Details")

@bookings_blueprint.route("/bookings/<id>/delete")
def delete_booking(id):
    booking_repository.delete_one(id)
    return redirect("/bookings")