from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime, timedelta

# flask --app 03_api run --debug
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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

database_metadata = {
    'projections_data_max_id': 0
}
projections_data = {}

@app.route('/projections', methods=['GET'])
def projections_get():
    return jsonify(projections_data)

def create_projection_id():
    projection_id = database_metadata['projections_data_max_id']
    database_metadata['projections_data_max_id'] += 1
    return projection_id

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
    projection_id = create_projection_id()
    projections_data[projection_id] = projection
    return projection_id

def init_db():
    create_projection('Terminator', '2023-09-17 15:30:00.000', 107, 'I will be back')
    create_projection('Terminator 2', '2023-09-17 18:30:00.000', 137, 'Hasta la vista, baby')
    create_projection('Oppenheimer', '2023-09-17 18:30:00.000', 180, 'Nastudovat si významné fyziky 20. století')

init_db()

@app.route('/projections/<int:projection_id>', methods=['GET'])
def projection_get(projection_id):
    if projection_id not in projections_data:
        return "Page not found", 404
    return jsonify(projections_data[projection_id])

@app.route('/projections/<int:projection_id>', methods=['DELETE'])
def projection_delete(projection_id):
    if projection_id not in projections_data:
        return "Page not found", 404
    projections_data.pop(projection_id)
    return "Projection removed"

def update_projection(projection_id, name, start_time, duration, description):
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
    projections_data[projection_id] = projection


def valid_projection_json(data):
    for field in ['name', 'start_time', 'duration', 'description']:
        if field not in data:
            return False
    return True

# Example json for the new event
# {
#   "description": "Popkulturní klasika no 2",
#   "duration": 99,
#   "name": "Rambo 2",
#   "start_time": "2023-09-17 18:30:00.000"
# }
@app.route('/projections/<int:projection_id>', methods=['PUT'])
def projection_put(projection_id):
    if projection_id not in projections_data:
        return "Page not found", 404
    content = request.json
    if not valid_projection_json(content):
        return "Invalid projection JSON", 400
    update_projection(
        projection_id,
        content['name'],
        content['start_time'],
        content['duration'],
        content['description'],
    )
    return jsonify(projections_data[projection_id])

@app.route('/projections', methods=['POST'])
def projections_post():
    content = request.json
    if not valid_projection_json(content):
        return "Invalid projection JSON", 400
    projection_id = create_projection(
        content['name'],
        content['start_time'],
        content['duration'],
        content['description'],
    )
    return f'New projectionn with ID: {projection_id} created'