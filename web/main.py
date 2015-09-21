# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, url_for, make_response, session, redirect
from flask import flash, Response

from pymongo import Connection
from werkzeug.security import generate_password_hash, check_password_hash
from login import is_new_user, insert, check_password, get_password
from datetime import timedelta
from werkzeug import secure_filename
import os
from tempfile import mktemp

app = Flask(__name__)
app.secret_key = 'some_secret'
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    session.permanent = True
    print session
    if 'username' in session:
        return render_template("index.html")
    return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    print "hah"
    if request.method == "POST":
        # handle form request
        username = request.form["username"]
        password = request.form["password"]
        connection = Connection()
        db = connection['user_pwd']
        post = db.post
        print "2333333333"
        if is_new_user(post, username) is True:
            #insert(post, username, password)
            return "请先注册"
        db_password = get_password(post, username)
        if check_password_hash(db_password, password) is True:
            print "inin"
            '''
            flash(username)
            resp = make_response("main html")
            resp.set_cookie('username', username)
            '''
            session['username'] = request.form['username']
            res = Response('add cookies')
            import time
            res.set_cookie(key=username, value='letian', expires=time.time()+6*60)
            return res
            #return resp
        return "用户名或密码错误"
    url_for('static', filename='basic.css')
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    print "sign"
    if request.method == "POST":

        username = request.form["u"]
        password = request.form["p"]
        connection = Connection()
        db = connection['user_pwd']
        post = db.post
        insert(post, username, password)
        return redirect(url_for('set_info'))
    print "2333"
    url_for('static', filename='basic.css')
    url_for('static', filename='1.jpg')
    return render_template("signup.html")


@app.route("/set_info", methods=["GET", "POST"])
def set_info():
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    print "haha"
    if request.method == "POST":
        print "1"
        f = request.files['photo']
        fname = mktemp(suffix='_', prefix='u', dir=UPLOAD_FOLDER) + secure_filename(f.filename)
        f.save("/home/shennina/web/2.jpg")
        return "yes"

    url_for('static', filename='edit.css')
    return render_template("edit.html")
if __name__ == "__main__":
    app.run(host='localhost', port=8080,debug=True)