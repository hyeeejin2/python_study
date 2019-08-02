<<<<<<< HEAD
from flask import Flask, render_template, request, url_for, redirect
=======
from flask import Flask, render_template, request
>>>>>>> 402f6ed3bdab100209d9d62d1aee76f51eadf0d1
import pymysql

app=Flask(__name__)
app.debug=True
    
@app.route("/tutee_login")
<<<<<<< HEAD
@app.route("/tutee_login/<error>")
def tutee_login(error=None):
    return render_template("login.html",error=error)

@app.route("/login_test", methods=["POST","GET"])
def login_test():
=======
def login():
    return render_template("login.html")

@app.route("/login_success", methods=["POST","GET"])
def login_success():
>>>>>>> 402f6ed3bdab100209d9d62d1aee76f51eadf0d1
    if request.method=="POST":
        email=request.form["email"] # POST 방식으로 form의 변수 값을 읽는다
        pw=request.form["pw"]

<<<<<<< HEAD
        db=pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='0507', db='attendance', charset='utf8')
=======
        db=pymysql.connect(host='192.168.109.149', port=3306, user='admin', password='0507', db='attendance', charset='utf8')
>>>>>>> 402f6ed3bdab100209d9d62d1aee76f51eadf0d1
        cursor=db.cursor()

        query="SELECT name FROM tutee_info WHERE email=%s AND pw = %s;"
        value=(email, pw)

        cursor.execute(query, value)
        data=(cursor.fetchall())

<<<<<<< HEAD
        cursor.close()
        db.close()

        for row in data:
            data=row[0]
        if data:
            return redirect(url_for('login_success'))
        else:
            error='email or password error!'
            return redirect(url_for('tutee_login',error=error))

@app.route("/login_success")
def login_success():
    return "login_success"
=======
        for row in data:
            data=row[0]
        if data:
            return data
        else:
            return "None data"

        cursor.close()
        db.close()
    else:
        email=request.args.get("email") # GET 방식으로 form의 변수 값을 읽는다
        pw=request.args.get("pw")
        return "%s님 로그인 됐습니다!!" % email
>>>>>>> 402f6ed3bdab100209d9d62d1aee76f51eadf0d1

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup_success",methods=["POST","GET"])
def signup_success():
    if request.method=="POST":
        id_=request.form["name"]
        pw=request.form["pw"]
        phone=request.form["phonenum"]
        email=request.form["email"]
        return "signup !! \n ID is %s pw is %s \n phone number is %s email is %s\n " % (id_,pw,phone,email)
    else:
        id_=request.args.get("name")
        pw=request.args.get("pw")
        phone=request.args.get("phonenum")
        email=request.args.get("email")
<<<<<<< HEAD
        return "signup !! \n ID is %s pw is %s \n phone number is %s email is %s\n " % (id_,pw,phone,email)
=======
        return "signup !! \n ID is %s pw is %s \n phone number is %s email is %s\n " % (id_,pw,phone,email)
>>>>>>> 402f6ed3bdab100209d9d62d1aee76f51eadf0d1
