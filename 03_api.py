from flask import Flask

# flask --app 03_api run --debug
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/error")
def error():
    return f"1 / 0 = {1/0}"

@app.route('/param/<parameter>')
def param(parameter):
    return f'Parameter: {parameter}, Type: {type(parameter)}'

@app.route('/param_int/<int:parameter>')
def param_int(parameter):
    return f'Int Parameter: {parameter}, Type: {type(parameter)}'

@app.route('/param_float/<float:parameter>')
def param_float(parameter):
    return f'Float Parameter: {parameter}, Type: {type(parameter)}'

@app.route('/param_string/<string:parameter>')
def param_string(parameter):
    return f'String Parameter: {parameter}, Type: {type(parameter)}'