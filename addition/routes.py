from flask import Blueprint,render_template,request

add = Blueprint("addition",__name__,template_folder="templates")

@add.route("/add")
def index():
  return render_template("addition.html")

@add.route("/addnum",methods=['POST'])
def addnum():
  num1 = int(request.form['num1'])
  num2 = int(request.form['num2'])
  res = num1 + num2
  return render_template("addition.html",result = res)