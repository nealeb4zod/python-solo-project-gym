from flask import render_template, request, redirect
from flask import Blueprint
from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

instructors_blueprint = Blueprint("instructors", __name__)

@instructors_blueprint.route("/instructors")
def instructors_index():
    instructors = instructor_repository.get_all()
    return render_template("instructors/index.html", instructors=instructors, title="Instructors")

@instructors_blueprint.route("/instructors/new")
def new_instructor_form():
    return render_template("instructors/new.html", title="New Instructor")

@instructors_blueprint.route("/instructors", methods=["POST"])
def create_instructor():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    new_instructor = Instructor(first_name, last_name, date_of_birth, address, phone_number)
    instructor_repository.new(new_instructor)
    return redirect("/instructors")

@instructors_blueprint.route("/instructors/<id>/edit")
def edit_instructor(id):
    instructor = instructor_repository.get_one(id)
    return render_template("/instructors/edit.html", instructor=instructor, title="Edit Instructor Details")

@instructors_blueprint.route("/instructors/<id>", methods=["POST"])
def update_instructor(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    updated_instructor = Instructor(first_name, last_name, date_of_birth, address, phone_number, id)
    instructor_repository.edit(updated_instructor)
    return redirect("/instructors")

@instructors_blueprint.route("/instructors/<id>")
def show_details(id):
    instructor_activities = instructor_repository.get_activities(id)
    instructor = instructor_repository.get_one(id)
    return render_template("/instructors/show.html", instructor=instructor, instructor_activities=instructor_activities, title="Instructor Details")

@instructors_blueprint.route("/instructors/<id>/delete")
def delete_instructor(id):
    instructor_repository.delete_one(id)
    return redirect("/instructors")