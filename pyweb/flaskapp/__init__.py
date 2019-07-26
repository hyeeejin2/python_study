from flask import Flask, g, Response, make_response,redirect, url_for, redirect, request, render_template

app=Flask(__name__)
app.debug=True # true로 하는게 오류를 좀 더 많이 보여준다

@app.before_request # 요청 처리 전에 실행하는 것
def before_request():
    print("before_request!")
    g.str="한글" #g객체는 application context 영역

# 동적 URI
@app.route("/profile/<username>")
def get_profile(username):
    return "profile : "+username

@app.route("/number/<float:num>")
def get_intnumber(num):
    return "number : %d" % num

# redirect, url_for()
@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s as Guest" % guest

@app.route("/user/<name>")
def hello_user(name):
    if name=="admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))

# request form, args
@app.route("/main")
def main():
    return render_template("login.html") # html 파일을 렌더링

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" % name

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["myName"] # POST 방식으로 form의 myName변수 값을 읽는다
        return redirect(url_for("success", name=user))
    else:
        user=request.args.get("myName") # GET 방식으로 form의 myName변수 값을 읽는다
        return redirect(url_for("success", name=user))

# Response Objects
@app.route("/res1")
def res1():
    custom_res=Response("Custom Response",200,{'test':'ttt'}) #(데이터, http 상태코드, json->은밀하게 보낼 때 사용)
    return make_response(custom_res) # make_response -> 큰 데이터를 응답할 때 사용

@app.route("/") #request에 대한
def helloworld():
    return "Hello World!" #reponse, 아무것도 안하고 문자열만 보내므로 string response 객체임

# Global Object 
@app.route("/g") #route는 URI를 정의함
def helloworld2():
    return "Hello World!!"+getattr(g,'str','111') #str값이 없으면 111(default)
    #g는 접속자 수, 실시간 접속자 수를 체크할 수 있음 (증가연산자 이용해서)
    #g.str="한글"이라고 선언하면 'srt'은 다 한글인 점을 이용해서 g는 나한테 붙은 사람들을 컨트롤 하고 싶을 때도 사용 가능
     