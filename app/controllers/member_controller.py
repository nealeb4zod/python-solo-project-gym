from flask import Flask, render_template, request, redirect
from flask import Blueprint

from app.models.member import Member

import app.repositories.member_repository as member_repository
import app.repositories.membership_type_repository as membership_type_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.get_all()
    return render_template("members/index.html", members=members, title="Members")

@members_blueprint.route("/members/add")
def new_member():
    membership_types = membership_type_repository.get_all()
    return render_template("members/new.html", membership_types=membership_types, title="New Member")