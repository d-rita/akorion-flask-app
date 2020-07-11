### Flask app to send order to email.

##### To get the project:
- Clone the project using `git clone https://github.com/d-rita/akorion-flask-app.git`
- Change to the project folder using `cd akorion-flask-app`
- While in the main directory, create a virtual environment using `virtualenv venv`
- activate the virtual environment with `source ./venv/bin/activate`
- run `pip install -r requirements.txt` to install dependencies
- Following the `.env.sample` file, create a `.env` file and fill in the values

##### App implementation:

This is the 2nd implementation for this app. It is purely a backend solution, and is best tested with an app like Postman. In this case, the data required from the user is got through a JSON object. This API solution can be consumed by a separately designed frontend application. 

###### For version 2:
- switch to the version-two branch using: `git checkout version-two`
- Set Flask app to app.py using `export FLASK_APP=application.py`
- Open postman, and type in the url "http://127.0.0.1:5000/", choose the `POST` method
- Fill in the raw data as a JSON object: 
    ```json  
        {
            "first_name": "Diana",
            "last_name": "Nanyanzi",
            "phone": "070012345",
            "order": "pesticide"
        }
    ```
and submit.

Notes:
- The sender and recipient emails can be altered to fit your own. 
- With Gmail, you have to let less secure apps access your email before it can successfully send emails with your account. 
