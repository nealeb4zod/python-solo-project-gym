from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint

from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository


bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.get_all()
    return render_template("bookings/index.html", bookings=bookings, title="Bookings")

@bookings_blueprint.route("/bookings/new/member/<id>")
def new_member_booking(id):
    member = member_repository.get_one(id)
    activities = activity_repository.get_all()
    return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking")

@bookings_blueprint.route("/bookings/new/activity/<id>")
def new_activity_booking(id):
    activity = activity_repository.get_one(id)
    members = member_repository.get_all()
    return render_template("bookings/new-activity.html", activity=activity, members=members, title="New Booking")

@bookings_blueprint.route("/bookings/activity", methods=["POST"])
def create_booking():

    activity_id = request.form["activity"]
    member_id = request.form["member"]
    activity = activity_repository.get_one(activity_id)
    member = member_repository.get_one(member_id)

    new_booking = Booking( activity, member )
    booking_repository.new(new_booking)
    return redirect ("/activities")

@bookings_blueprint.route("/bookings/<id>/delete")
def delete_booking(id):
    booking_repository.delete_one(id)
    return redirect("/bookings")