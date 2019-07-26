from flask import Flask, render_template, request

app=Flask(__name__)
app.debug=True

@app.route("/main")
def main():
    return render_template("login.html")

@app.route("/login")
def login():
    if request.method=="POST":
        phone=request.form["phone"] # POST 방식으로 form의 변수 값을 읽는다
        pw=request.form["pw"]
        return "login !! \n phone number is %s \n pw is %s" % (phone,pw)
    else:
        phone=request.args.get("phone") # GET 방식으로 form의 변수 값을 읽는다
        pw=request.args.get("pw")
        return "login !! \n phone number is %s \n pw is %s" % (phone,pw)


