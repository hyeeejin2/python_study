from flask import Flask, app, render_template, request, url_for, redirect, session, escape
from datetime import timedelta
import pymysql, json, hashlib

app=Flask(__name__)
app.debug=True
app.secret_key="temporary string"

@app.before_request
def befor_request():
    session.permanent=True
    app.permanent_session_lifetime=timedelta(minutes=30)

@app.route("/main")
def main():
    string={'page':'main'}
    return json.dumps(string)

@app.route("/tutee_login")
@app.route("/tutee_login/<error>")
def tutee_login(error=None):
    return render_template("login.html",error=error)

@app.route("/login_test", methods=["POST"])
def login_test():
    error=None
    if request.method=="POST":
        email=request.form["email"]
        pw=request.form["pw"]
        pw=pw.encode()
        hash_pw=hashlib.sha256(pw).hexdigest()

        db=pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='0507', db='attendance', charset='utf8')
        cursor=db.cursor()

        query="SELECT name FROM tutee_info WHERE email=%s AND pw =%s;"
        value=(email, hash_pw)
        
        cursor.execute(query, value)
        data=(cursor.fetchall())
        
        cursor.close()
        db.close()
        
        for row in data:
            data=row[0]
        
        if data:
            session['username']=request.form['email']
            return redirect(url_for('session_check'))

        else:
            error={'error':'error'}
            json.dumps(error)
            return redirect(url_for('tutee_login',error=error))

@app.route("/session_check")
def session_check():
    if 'username' in session:
        return redirect(url_for('login_success'))

    else:
        error={'error':'session error'}
        json.dumps(error)
        return redirect(url_for('tutee_login',error=error))

@app.route("/login_success")
def login_success():
    if 'username' in session:
        message={'message':'%s login success' % escape(session['username'])}
        return json.dumps(message)
    else:
        error={'error':'error'}
        json.dumps(error)
        return redirect(url_for('tutee_login',error=error))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route("/tutee_signup")
@app.route("/tutee_signup/<error>")
def tutee_signup(error=None):
    return render_template("signup.html",error=error)

@app.route("/signup_test",methods=["POST"])
def signup_test():
    if request.method=="POST":
        name=request.form["name"]
        pw=request.form["pw"]
        pw=pw.encode()
        hash_pw=hashlib.sha256(pw).hexdigest()
        email=request.form["email"]
        mac_address=request.form["mac_address"]
        
        db=pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='0507', db='attendance', charset='utf8')
        cursor=db.cursor()

        query = "SELECT name FROM tutee_info WHERE email=%s;"
        value=(email)

        cursor.execute(query,value)
        data=(cursor.fetchall())
        
        for row in data:
            data=row[0]

        if data:
            error={'error':'email error!'}
            json.dumps(error)
            return redirect(url_for('tutee_signup',error=error))
        
        else:
            query="SELECT auto_increment FROM information_schema.tables WHERE table_name = 'tutee_info';"
            cursor.execute(query)
            num=(cursor.fetchall())

            for row in num:
                num=row[0]

            query="INSERT INTO tutee_info VALUES(%s, %s, %s, %s, %s)"
            value=(int(num), name, hash_pw, email, mac_address)

            cursor.execute(query, value)
            data=(cursor.fetchall())

            query="set @cnt=0;"
            cursor.execute(query)

            query="update tutee_info set tutee_info.no=@cnt:=@cnt+1;"
            cursor.execute(query)

            if not data:
                db.commit()
                return redirect(url_for('signup_success'))
            else:
                db.rollback()
                error={'error':'signup failed!'}
                json.dumps(error)
                return redirect(url_for('tutee_signup',error=error))

        cursor.close()
        db.close()

@app.route("/signup_success")
def signup_success():
    message={'message':"signup success"}
    return json.dumps(message)

@app.route("/test")
def test():
    db=pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='0507', db='attendance', charset='utf8')
    cursor=db.cursor()

    query="SELECT name, pw, email FROM tutee_info"

    cursor.execute(query)
    data=(cursor.fetchall())

    data_dic=[]
    for row in data:
        dic={'name':row[0],'pw':row[1], 'email':row[2]}
        data_dic.append(dic)

    return json.dumps(data_dic)
