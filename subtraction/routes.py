from flask import Blueprint, render_template, request

sub = Blueprint("subtraction",__name__,template_folder="templates")

@sub.route("/sub")
def index():
  return render_template("subtraction.html")

@sub.route("/subnum",methods=['POST'])
def subnum():
  resp = request.form.to_dict(flat=True)
  num1 = int(resp['num1'])
  num2 = int(resp['num2'])
  resub = num1 - num2
  return render_template("subtraction.html",result = resub)