from flask import Flask, render_template, request, redirect
from flask import Blueprint

from app.models.member import Member

import app.repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.get_all()
    return render_template("members/index.html", members=members)