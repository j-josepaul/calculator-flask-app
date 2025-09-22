from flask import Blueprint, render_template, request

mul = Blueprint("multiply",__name__,template_folder="templates")

@mul.route("/mul")
def index():
  return render_template("multiplication.html")

@mul.route("/mulnum",methods=['POST'])
def mulnum():
  num1 = int(request.form['num1'])
  num2 = int(request.form['num2'])
  res = num1 * num2
  return render_template("multiplication.html",result = res)