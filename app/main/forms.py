"""
Module described forms
"""
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
import re


class EditCollection(FlaskForm):
    choice = ["user_email", "user_phone", "order_date", "comment"]
    name = StringField("name", validators=[DataRequired()])
    field1_name = RadioField("field1_type", choices=choice, validate_choice=False)
    field1_value = StringField("field1_value", validators=[DataRequired()])
    field2_name = RadioField("field2_type", choices=choice, validate_choice=False)
    field2_value = StringField("field2_value", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_field1_value(self, field):
        if self.field1_name.data == "user_email":
            pattern = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
            if re.match(pattern, field.data) is None:
                raise ValidationError("Wrong email")
        elif self.field1_name.data == "user_phone":
            pattern = "^\+7 \d{3} \d{3} \d{2} \d{2}$"
            if re.match(pattern, field.data) is None:
                raise ValidationError("Wrong phone")
        elif self.field1_name.data == "order_date":
            pattern1 = "^\d{2}\.\d{2}\.\d{4}$"
            pattern2 = "^\d{4}-\d{2}-\d{2}$"
            if re.match(pattern1, field.data) is None or re.match(pattern2, field.data) is None:
                raise ValidationError("Wrong date")
            else:
                try:
                    if field.data[2] == ".":
                        datetime.strptime(field.data, "%d.%m.%Y")
                    else:
                        datetime.strptime(field.data, "%Y-%m-%d")
                except:
                    raise ValidationError("Wrong date")

    def validate_field2_value(self, field):
        if self.field2_name.data == "email":
            pattern = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
            if re.match(pattern, field.data) is None:
                raise ValidationError("Wrong email")
        elif self.field2_name.data == "phone":
            pattern = "^\+7 \d{3} \d{3} \d{2} \d{2}$"
            if re.match(pattern, field.data) is None:
                raise ValidationError("Wrong phone")
        elif self.field2_name.data == "date":
            pattern1 = "^\d{2}\.\d{2}\.\d{4}$"
            pattern2 = "^\d{4}-\d{2}-\d{2}$"
            if re.match(pattern1, field.data) is None or re.match(pattern2, field.data) is None:
                raise ValidationError("Wrong date")
            else:
                try:
                    if field.data[2] == ".":
                        datetime.strptime(field.data, "%d.%m.%Y")
                    else:
                        datetime.strptime(field.data, "%Y-%m-%d")
                except:
                    raise ValidationError("Wrong date")


class TestForm(FlaskForm):
    # choice = ["user_email", "user_phone", "order_date", "comment"]
    # field1_name = RadioField("field1_type", choices=choice, validate_choice=False)
    field1_name = StringField("field1_type", validators=[DataRequired()])
    field1_value = StringField("field1_value", validators=[DataRequired()])
    # field2_name = RadioField("field2_type", choices=choice, validate_choice=False)
    field2_name = StringField("field2_type", validators=[DataRequired()])
    field2_value = StringField("field2_value", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AutoForm(FlaskForm):
    submit =SubmitField("Populate")
