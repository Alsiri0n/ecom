from app.main import bp
from flask import render_template, url_for, current_app, request, flash, redirect
from .forms import EditCollection, TestForm, AutoForm
from app.mongo import populate


@bp.route("/", methods=["GET", "POST"])
def index():
    form = AutoForm()
    if form.validate_on_submit():
        populate()
    return render_template("index.html", form=form)


@bp.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditCollection()
    if form.validate_on_submit():
        data = {"name": form.name.data,
                form.field1_name.data: form.field1_value.data,
                form.field2_name.data: form.field2_value.data}
        current_app.db.test_coll.insert_one(data)
        flash("Data updated")
        # return redirect(url_for("main.view"))
    return render_template("edit.html", form=form)


@bp.route("/view/<string:coll_name>")
@bp.route("/view")
def view(coll_name: str = ""):
    if coll_name == "":
        my_coll = current_app.db.list_collection_names()
    else:
        my_coll = current_app.db.test_coll.find()
    return render_template("view.html", coll=my_coll)


@bp.route("/test")
def test():
    form = TestForm()
    return render_template("test.html", form=form)
