from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.activity import Activity

import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.get_all()
    return render_template("activities/index.html", activities=activities, title="Activities")

@activities_blueprint.route("/activities/new")
def new_activity():
    return render_template("activities/new.html", title="New Activity")

@activities_blueprint.route("/activities", methods=["POST"])
def create_activity():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]

    new_activity = Activity(first_name, last_name, date_of_birth, address, phone_number)
    activity_repository.new(new_activity)
    return redirect("/activities")

@activities_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    activity = activity_repository.get_one(id)
    return render_template("/activities/edit.html", activity=activity, title="Edit Activity Details")

@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]

    updated_activity = Activity(first_name, last_name, date_of_birth, address, phone_number, id)
    activity_repository.edit(updated_activity)
    return redirect("/activities")

@activities_blueprint.route("/activities/<id>")
def show_details(id):
    activity_members = activity_repository.get_members(id)
    activity = activity_repository.get_one(id)
    instructor = instructor_repository.get_one(activity.instructor)
    return render_template("/activities/show.html", activity=activity, instructor=instructor, activity_members=activity_members, title="Activity Details")

@activities_blueprint.route("/activities/<id>/delete")
def delete_activity(id):
    activity_repository.delete_one(id)
    return redirect("/activities")