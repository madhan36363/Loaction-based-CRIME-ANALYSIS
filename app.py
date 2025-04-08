from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management



# ✅ Dummy user credentials for login
USER_CREDENTIALS = {"admin": "123"}

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        session["user"] = username
        return redirect(url_for("home"))
    return "Invalid credentials! <a href='/'>Try Again</a>"

@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html")
    return redirect(url_for("login_page"))

@app.route("/complaint")
def complaint():
    return render_template("complaint.html")

@app.route("/rules")
def rules():
    if "user" in session:
        return render_template("rules.html")
    return redirect(url_for("login_page"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login_page"))

if __name__ == "__main__":
    app.run(debug=True)