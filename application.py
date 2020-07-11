import os

from flask import Flask, make_response, jsonify, request
from dotenv import find_dotenv, load_dotenv
from flask_mail import Mail, Message

# create Flask app instance
app = Flask(__name__)

# locate env file
load_dotenv(find_dotenv())

# set app configurations
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

# configure Mail to work with the app
mail = Mail(app)

# validate data entered
def validate(string):
    response = ""
    if not string:
        response = None
    elif not isinstance(string, str):
        response = None
    else:
        response = string
    return response

@app.route('/', methods=["POST"])
def place_order():
    try:
    # retrieve valid json data
        data = request.get_json() #to do: validate for json data
        first_name = validate(data['first_name'])
        last_name = validate(data['last_name'])
        phone = validate(data['phone'])
        order = validate(data['order'])
    except TypeError:
        return make_response(jsonify({ 'message': f"Please enter JSON data"}), 400)
    except KeyError as e:
        return make_response(jsonify({ 'message': f"Please fill in the {e} field."}), 400)

    # customise error responses
    if order is None:
        return make_response(jsonify({'message': 'Please fill in order'}), 400)
    elif phone is None:
        return make_response(jsonify({ 'message': "Please fill in phone number"}), 400)
    elif last_name is None or first_name is None:
        return make_response(jsonify({'message': 'Please fill in your first and last names'}), 400)

    #send data to email
    try:
        email = Message(
        subject="Customer Order",
            body=f"Customer: {first_name} {last_name} has placed an order for {order}. Contact them on {phone}.",
            sender=os.environ.get("MAIL_USERNAME"),
            recipients=[os.environ.get("MAIL_RECIPIENT")]
        )
        mail.send(email)
        return make_response(jsonify({ 'message': 'Your order has been placed'}), 201)
    except:
        return make_response(jsonify({'message': 'Authentication error. Please provide the right credentials'}), 400)
