from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime, timedelta

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

# CRUD -> HTTTP methods
# Create -> POST
# Read -> GET
# Update -> PUT
# Delete -> DELETE

projections_data = {}

@app.route('/projections', methods=['GET'])
def projections_get():
    return jsonify(projections_data)

def create_projection(name, start_time, duration, description):
    """
    Parameters:
        name (str): name of the projection
        start_time (str): start time of the projection in ISO format (e.g. 2011-11-04 00:05:23.283)
        duration (int): duration of projection in minutes
    """
    start_time = datetime.fromisoformat(start_time)
    duration = timedelta(minutes=duration)
    end_time = start_time + duration
    projection = {
        'name': name,
        'start_time': start_time,
        'end_time': end_time,
        # 'duration': duration,
        'description': description
    }
    projections_data[0] = projection

create_projection('Terminator', '2023-09-17 15:30:00.000', 107, 'I will be back')