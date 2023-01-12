from app.main import bp
from flask import render_template, url_for, current_app, g


@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@bp.route("/edit")
def edit():
    return render_template("edit.html")


@bp.route("/view/<string:coll_name>")
@bp.route("/view")
def view(coll_name: str = ""):
    if coll_name == "":
        my_coll = current_app.db.list_collection_names()
        # return render_template("view.html", coll={"name": ""})
    else:
        my_coll = current_app.db.test_coll.find()
    return render_template("view.html", coll=my_coll)