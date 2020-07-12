import os

from flask import Flask, render_template, request, make_response, jsonify
from dotenv import find_dotenv, load_dotenv
from flask_mail import Mail, Message

app = Flask(__name__)

load_dotenv(find_dotenv())

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)

@app.route('/')
def index():
    # render form 
    return render_template('index.html')

@app.route('/order', methods=["POST"])
def submit_order():
    # get form data
    name = request.form["username"]
    tel = request.form["phone"]
    order_name = request.form["order"]

    # validate data
    if name == "" or tel == "" or order_name == "":
        return make_response(jsonify("Fill in all values in the form"), 400)

    # send valid data to email
    try:
        email = Message(
        subject="Customer Order",
            body=f"Hello Customer support. An order for {order_name} has been placed by {name}. Contact them on: {tel}.",
            sender=os.environ.get("MAIL_USERNAME"),
            recipients=[os.environ.get("MAIL_RECIPIENT")]
        )
        mail.send(email)
        return make_response(render_template('final.html', name=name, tel=tel, order_name=order_name), 200)
    except:
        # to-do: contact support with error message
        return make_response(render_template('error.html'), 400)
