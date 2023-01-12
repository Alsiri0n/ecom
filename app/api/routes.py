# from app import db
from flask import request, jsonify, current_app, make_response
from app.api import bp
import re
from datetime import datetime


@bp.route("/get_form", methods=["GET", "POST"])
def get_form():
    if request.method == "POST":
        print(request)
        f1 = [request.form["field1_name"], request.form["field1_value"]]
        f2 = [request.form["field2_name"], request.form["field2_value"]]
        for f in [f1, f2]:
            if f[0] == "user_email":
                pattern = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
                if re.match(pattern, f[1]) is None:
                    return make_response(jsonify([f1, f2], 200))
            elif f[0] == "user_phone":
                pattern = "^\+7 \d{3} \d{3} \d{2} \d{2}$"
                if re.match(pattern, f[1]) is None:
                    return make_response(jsonify([f1, f2], 200))
            elif f[0] == "order_date":
                pattern1 = "^\d{2}\.\d{2}\.\d{4}$"
                pattern2 = "^\d{4}-\d{2}-\d{2}$"
                if re.match(pattern1, f[1]) is None or re.match(pattern2, f[1]) is None:
                    try:
                        if f[1][2] == ".":
                            datetime.strptime(f[1], "%d.%m.%Y")
                        else:
                            datetime.strptime(f[1], "%Y-%m-%d")
                    except:
                        return make_response(jsonify([f1, f2], 200))
        data = list(current_app.db.test_coll.find({f1[0]: {"$exists": 1}, f2[0]: {"$exists": 1}}, {"_id": 0, "name": 1}))
        if not data:
            data = [f1, f2]
        return make_response(jsonify(data, 200))
    else:
        return make_response(jsonify("{Method: get}", 200))
