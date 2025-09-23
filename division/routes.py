from flask import Blueprint, render_template,request

div = Blueprint("division",__name__,template_folder="templates")

@div.route("/div")
def index():
  return render_template("division.html")

@div.route("/divnum",methods=['POST'])
def divnum():
  num1 = int(request.form['num1'])
  num2 = int(request.form['num2'])
  res = num1 / num2
  return render_template("division.html",result = res)