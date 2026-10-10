import os
import smtplib
from email.message import EmailMessage

import requests
from flask import Flask, render_template, request, abort

POSTS_URL = "https://api.npoint.io/b08b04a80ea3d505563c"

# Set these as environment variables (PyCharm: Run > Edit Configurations > Environment variables)
# OWN_EMAIL      = the Gmail address that sends AND receives the contact messages
# OWN_PASSWORD   = a Google "App Password" (not your normal Gmail password)
OWN_EMAIL = os.environ.get("OWN_EMAIL")
OWN_PASSWORD = os.environ.get("OWN_PASSWORD")

app = Flask(__name__)


def get_posts():
    return requests.get(POSTS_URL, timeout=10).json()


def send_email(name, email, phone, message):
    msg = EmailMessage()
    msg["Subject"] = f"New message from {name} (blog contact form)"
    msg["From"] = OWN_EMAIL
    msg["To"] = OWN_EMAIL
    msg["Reply-To"] = email
    msg.set_content(f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}")
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.send_message(msg)


@app.route('/')
def home():
    return render_template("index.html", all_posts=get_posts())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        try:
            send_email(data["name"], data["email"], data["phone"], data["message"])
        except Exception as e:
            print("Could not send email:", e)
            return render_template("contact.html", msg_sent=False, error=True)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def post(index):
    requested_post = next((p for p in get_posts() if p["id"] == index), None)
    if requested_post is None:
        abort(404)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
