"""
AppName:Portfolio_test
purpose: server
"""
# Dependencies
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# Internal Modules
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Methods------------------------------
@app.route('/')
def home() -> str:
    """
    Takes user to Homepage of the Portfolio_test website
    """
    return render_template('index.html')


# ------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
