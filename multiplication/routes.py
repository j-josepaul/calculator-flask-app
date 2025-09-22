from flask import Blueprint, render_template

mul = Blueprint("multiply",__name__,template_folder="templates")

@mul.route("/div")
def index():
  return render_template("multiply.html")

