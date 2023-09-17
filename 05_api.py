from flask import Flask
from flask import request

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

# @app.route('/method') # -> jen GET
# @app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE', 'ABCD']) -> můžu si napsat co chci
@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def http_method():
    return f'HTTP method: {request.method}'

# @app.get('/method_2/<string:parameter>')
@app.route('/method_2/<string:parameter>', methods=['GET'])
def method_get(parameter):
    return f'GET with parameter: {parameter}'

# @app.post('/method_2/<string:parameter>')
@app.route('/method_2/<string:parameter>', methods=['POST'])
def method_post(parameter):
    return f'POST with parameter: {parameter}'

# @app.put('/method_2/<string:parameter>')
@app.route('/method_2/<string:parameter>', methods=['PUT'])
def method_put(parameter):
    return f'PUT with parameter: {parameter}'

# @app.delete('/method_2/<string:parameter>')
@app.route('/method_2/<string:parameter>', methods=['DELETE'])
def method_delete(parameter):
    return f'DELETE with parameter: {parameter}'