from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True

signup_form = """
<!DOCTYPE HTML>
<html>
    <head>
        <h1>Signup</h1>
       <style>
            form {{
                padding: 20px;
                width: 540px;
                line-height: 2;
                font: 16px serif;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
         <form action="/" method="post">
            <label> Username: </label>
            <input type="text" name="user"/>
            <br>
            <label> Password: </label>
            <input type="text" name="pass"/>
            <br>
            <label> Verify Password: </label>
            <input type="text" name="v_pass"/>
            <br>
            <label> Email (optional): </label>
            <input type="text" name="email"/>
            <br>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return signup_form.format("")

app.run()