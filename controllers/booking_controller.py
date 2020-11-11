from flask import render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.membership_type_repository as membership_type_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings_index():
    bookings = booking_repository.get_all()
    return render_template("bookings/index.html", bookings=bookings, title="Bookings")

@bookings_blueprint.route("/bookings/new/member/<id>")
def new_member_booking(id):
    member = member_repository.get_one(id)
    activities = activity_repository.get_all_active()
    return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking")

@bookings_blueprint.route("/bookings/new/activity/<id>")
def new_activity_booking(id):
    activity = activity_repository.get_one(id)
    members = member_repository.get_all_active()
    return render_template("bookings/new-activity.html", activity=activity, members=members, title="New Booking")

@bookings_blueprint.route("/bookings/activity", methods=["POST"])
def create_booking_from_activity():
    activity_id = request.form["activity"]
    member_id = request.form["member"]
    activity = activity_repository.get_one(activity_id)
    member = member_repository.get_one(member_id)
    member_membership_type = membership_type_repository.get_one(member.membership_type)
    activity_membership_type = membership_type_repository.get_one(activity.membership_type)
    current_bookings = len(activity_repository.get_members(activity_id))
    activities = activity_repository.get_all_active()
    if booking_repository.check_booking_exists(activity_id, member_id) == True:
        error = "Already booked!"
        return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking", error=error)
    elif member_membership_type.type == "Basic" and activity_membership_type.type == "Premium":
        error = "No basics!"
        return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking", error=error)
    elif current_bookings >= activity.capacity:
        error = "Activity Full!"
        return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking", error=error)
    else:
      new_booking = Booking( activity, member )
      booking_repository.new(new_booking)
      activity_page = "/activities/" + activity_id
      return redirect (activity_page)

@bookings_blueprint.route("/bookings/member", methods=["POST"])
def create_booking_from_member():
    activity_id = request.form["activity"]
    member_id = request.form["member"]
    activity = activity_repository.get_one(activity_id)
    member = member_repository.get_one(member_id)
    member_membership_type = membership_type_repository.get_one(member.membership_type)
    activity_membership_type = membership_type_repository.get_one(activity.membership_type)
    current_bookings = len(activity_repository.get_members(activity_id))
    activities = activity_repository.get_all_active()
    if booking_repository.check_booking_exists(activity_id, member_id) == True:
        error = "Already booked!"
        return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking", error=error)
    elif member_membership_type.type == "Basic" and activity_membership_type.type == "Premium":
        error = "No basics!"
        return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking", error=error)
    elif current_bookings >= activity.capacity:
        error = "Activity Full!"
        return render_template("bookings/new-member.html", member=member, activities=activities, title="New Booking", error=error)
    else:
        new_booking = Booking( activity, member )
        booking_repository.new(new_booking)
        member_page = "/members/" + member_id
        return redirect (member_page)

@bookings_blueprint.route("/bookings/<id>/delete")
def delete_booking(id):
    booking_repository.delete_one(id)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/delete/member/<member_id>/<activity_id>")
def delete_specific_booking_member(member_id,activity_id):
    booking_repository.delete_specific_booking(member_id,activity_id)
    member_page = "/members/" + member_id
    return redirect (member_page)

@bookings_blueprint.route("/bookings/delete/activity/<member_id>/<activity_id>")
def delete_specific_booking_activity(member_id,activity_id):
    booking_repository.delete_specific_booking(member_id,activity_id)
    activity_page = "/activities/" + activity_id
    return redirect (activity_page)