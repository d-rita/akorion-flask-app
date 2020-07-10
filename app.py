from flask import Flask, render_template, request, make_response

from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "nessareed12@gmail.com"
app.config["MAIL_PASSWORD"] = "dr18152229"
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
        return "Fill in all values in the form"

    # send valid data to email
    email = Message(
       subject="Customer Order",
        body=f"Customer: {name} has placed an order for {order_name}. This is their contact: {tel}",
        sender="nessareed12@gmail.com",
        recipients=["martinkatamba@akorion.com"]
    )
    mail.send(email)
    return render_template('final.html')
