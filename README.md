### Flask app to send order to email.

#### To get the project:
- Clone the project using `git clone https://github.com/d-rita/akorion-flask-app.git`
- Change to the project folder using `cd akorion-flask-app`
- While in the main directory, create a virtual environment using `virtualenv venv`
- activate the virtual environment with `source ./venv/bin/activate`
- run `pip install -r requirements.txt` to install dependencies
- Following the `.env.sample` file, create a `.env` file and fill in the values

#### App implementation: This is the first implementation for this app.

##### Version 1 (frontend + backend):
- It makes use of Jinja2 Templates, and can be tested by visiting the localhost url in a browser.

Steps:
- pull the version-one branch onto your local machine using `git pull origin version-one`
- switch to version-one branch using `git checkout version-one` in the terminal
- Set Flask app to app.py using `export FLASK_APP=app.py`
- run app using `flask run`
- go to http://127.0.0.1:5000/ and fill in the form and submit it. 

Notes:
- The sender and recipient emails can be altered to fit your own. 
- With Gmail, you have to let less secure apps access your email before it can successfully send emails with your account. 
