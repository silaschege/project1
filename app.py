from flask import Flask, render_template, request
from flaskext.mysql import MySQL


app= Flask(__name__)


app.config["MYSQL_DATABASE_USER"] = "project1"
app.config["MYSQL_DATABASE_PASSWORD"] = "qwerty1234"
app.config["MYSQL_DATABASE_DB"] = "project1"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql=MySQL()
mysql.init_app(app)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login_button", methods=["POST"])
def login_button():
           #Email = request.form['Email']
           #Pasword = request.form['Pasword']
           #if Email == " "  or Pasword == " ":
             # return render_template ("login.html", message = "enter data to empty fields")
           #cur = mysql.connection.cursor()
           cursor = mysql.get_db().cursor()
           cur.execute("SELECT * from login where Email" + Email + "and Pasword" + pasword + "")
           data = cur.fetchall()
           if data is None:
              return("User name or password is invalid")
           else:
              return render_template("success.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registrationbutton/<string:insert>",methods=["POST"])
def registration_button():
    cur =mysql.connection.cursor()
    if request.method == "POST":
        email = request.form["email"]
        password1 = request.form ["password1"]
        password2 = request.form ["password2"]
        if email == " " or password1 == " " or password2 == " ":
            return render_template("registration.html",message = "please enter required flieds")
        elif password1 != password2:
            return render_template("registration.html" , password_challange = "input matching passwords")
        elif password1 == password2:
            Pasword = password1
        return render_template("success.html")


if __name__ == "__main__":
    app.run(debug = True)
