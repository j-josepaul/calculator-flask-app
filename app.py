from flask import Flask,render_template
from addition.routes import add
from subtraction.routes import sub
from multiplication.routes import mul
from division.routes import div

app = Flask(__name__)
app.register_blueprint(add)
app.register_blueprint(sub)
app.register_blueprint(mul)
app.register_blueprint(div)

@app.route("/")
def index():
  return render_template("index.html")



if(__name__ == "admin"):
  app.run(debug=True)