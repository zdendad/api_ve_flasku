from flask import Flask

# flask --app 02_api run
# VS
# flask --app 02_api run --debug
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/error")
def error():
    return f"<p>1 / 0 = {1/0}</p>"