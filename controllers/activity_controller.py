from flask import  render_template, request, redirect
from flask import Blueprint
from dateutil.parser import parse
from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository
import repositories.membership_type_repository as membership_type_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def activities_index():
    activities = activity_repository.get_all_active()
    return render_template("activities/index.html", activities=activities, title="Activities")

@activities_blueprint.route("/activities/inactive")
def inactive_activities():
    activities = activity_repository.get_all_inactive()
    return render_template("activities/index.html", activities=activities, title="Activities")

@activities_blueprint.route("/activities/new")
def new_activity_form():
    instructors = instructor_repository.get_all()
    membership_types = membership_type_repository.get_all()
    return render_template("activities/new.html", instructors=instructors, membership_types=membership_types, title="New Activity")

@activities_blueprint.route("/activities", methods=["POST"])
def create_activity():
    name = request.form["name"]
    instructor_id = request.form["instructor"]
    date = request.form["date"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    membership_type_id = request.form["membership_type"]
    active = request.form["active"]
    datetime = date + " " + time
    date_time = parse(datetime,fuzzy=True)
    membership_type = membership_type_repository.get_one(membership_type_id)
    instructor = instructor_repository.get_one(instructor_id)
    new_activity = Activity(name, instructor, date_time, duration, capacity, membership_type, active)
    activity_repository.new(new_activity)
    return redirect("/activities")

@activities_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    instructors = instructor_repository.get_all()
    membership_types = membership_type_repository.get_all()
    activity = activity_repository.get_one(id)
    instructor = instructor_repository.get_one(activity.instructor)
    membership_type = membership_type_repository.get_one(activity.membership_type)
    return render_template("/activities/edit.html", activity=activity, instructor=instructor, membership_type=membership_type, instructors=instructors, membership_types=membership_types, title="Edit Activity Details")

@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    instructor_id = request.form["instructor"]
    date = request.form["date"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    membership_type_id = request.form["membership_type"]
    active = request.form["active"]
    datetime = date + " " + time
    date_time = parse(datetime,fuzzy=True)
    membership_type = membership_type_repository.get_one(membership_type_id)
    instructor = instructor_repository.get_one(instructor_id)
    updated_activity = Activity(name, instructor, date_time, duration, capacity, membership_type, active, id)
    activity_repository.edit(updated_activity)
    return redirect("/activities")

@activities_blueprint.route("/activities/<id>")
def show_details(id):
    activity = activity_repository.get_one(id)
    membership_type = membership_type_repository.get_one(activity.membership_type)
    activity_members = activity_repository.get_members(id)
    no_members_booked = len(activity_members)
    instructor = instructor_repository.get_one(activity.instructor)
    return render_template("/activities/show.html", activity=activity, instructor=instructor, activity_members=activity_members, no_members_booked=no_members_booked, membership_type=membership_type, title="Activity Details")

@activities_blueprint.route("/activities/<id>/delete")
def delete_activity(id):
    activity_repository.delete_one(id)
    return redirect("/activities")