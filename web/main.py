# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, url_for, make_response, session
from pymongo import Connection
from werkzeug.security import generate_password_hash, check_password_hash
from login import is_new_user, insert, check_password, get_password


app = Flask(__name__)


@app.route("/")
def index():
    username = request.cookies.get('username')
    print username
    resp = make_response("hah")
    resp.set_cookie('username', 'the username')
    return resp


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # handle form request
        username = request.form["username"]
        password = request.form["password"]
        connection = Connection()
        db = connection['user_pwd']
        post = db.post
        if is_new_user(post, username) is True:
            #insert(post, username, password)
            return "请先注册"
        db_password = get_password(post, username)
        if check_password_hash(db_password, password) is True:
            return "登录成功"
        return "用户名或密码错误"

    url_for('static', filename='basic.css')
    return render_template("login.html")


@app.route("/signup")
def sign_up():
    url_for('static', filename='basic.css')
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(host='localhost', port=8080,debug=True)