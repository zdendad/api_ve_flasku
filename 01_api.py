from flask import Flask

# flask --app 01_api run
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! 2</p>"