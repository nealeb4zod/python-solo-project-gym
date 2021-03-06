from flask import render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.membership_type_repository as membership_type_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members_index():
    members = member_repository.get_all_active()
    return render_template("members/index.html", members=members, title="Members")

@members_blueprint.route("/members/inactive")
def inactive_members():
    members = member_repository.get_all_inactive()
    return render_template("members/index.html", members=members, title="Members")

@members_blueprint.route("/members/new")
def new_member():
    membership_types = membership_type_repository.get_all()
    return render_template("members/new.html", membership_types=membership_types, title="New Member")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    email_address = request.form["email_address"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    membership_type_id = request.form["membership_type"]
    start_date = request.form["start_date"]
    active_membership = request.form["active_membership"]
    membership_type = membership_type_repository.get_one(membership_type_id)
    new_member = Member(first_name, last_name, date_of_birth, address, phone_number, email_address, membership_type, start_date, active_membership)
    member_repository.new(new_member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.get_one(id)
    membership_types = membership_type_repository.get_all()
    return render_template("/members/edit.html", member=member, membership_types=membership_types, title="Edit Member Details")

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    email_address = request.form["email_address"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    membership_type_id = request.form["membership_type"]
    start_date = request.form["start_date"]
    active_membership = request.form["active_membership"]
    membership_type = membership_type_repository.get_one(membership_type_id)
    updated_member = Member(first_name, last_name, date_of_birth, address, phone_number, email_address, membership_type, start_date, active_membership, id)
    member_repository.edit(updated_member)
    return redirect("/members")

@members_blueprint.route("/members/<id>")
def show_details(id):
    member = member_repository.get_one(id)
    booked_activities = member_repository.get_activities(id)
    membership_type = membership_type_repository.get_one(member.membership_type.id)
    return render_template("/members/show.html", member=member, membership_type=membership_type, booked_activities=booked_activities, title="Member Details")

@members_blueprint.route("/members/<id>/delete")
def delete_member(id):
    member_repository.delete_one(id)
    return redirect("/members")