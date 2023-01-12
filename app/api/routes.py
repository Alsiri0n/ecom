# from app import db
from flask import request, jsonify, current_app
from app.api import bp


@bp.route("/get_form", methods=["GET", "POST"])
def get_form():
    if request.method == "POST":
        pass
    else:
        return jsonify("{Method: get}")
