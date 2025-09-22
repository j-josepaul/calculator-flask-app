from flask import Blueprint, render_template

div = Blueprint("division",__name__,template_folder="templates")

@div.route("/div")
def index():
  return render_template("division.html")