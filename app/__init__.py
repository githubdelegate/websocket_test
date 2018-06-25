from datetime import time
from flask import Flask, request
from flask_socketio import SocketIO, emit, send

socketio = SocketIO()



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    register_bluepint(app)
    handle_socketio(app)
    return app


def register_bluepint(app):
    from app.api.user import api
    app.register_blueprint(api)


def handle_socketio(app):
    socketio.init_app(app)


# @app.route('/api/userlist')
# def index():
#     # return render_template('index.html')
#     d = {'error': 0, 'result': ['zy', 'nj']}
#     return jsonify(d)


@socketio.on('client_event')
def client_msg(msg):
    print('msg')
    emit('server_response', {'data': msg['data']})


@socketio.on('connect_event')
def connected_msg(msg):
    print('connect')
    emit('server_response', {'data': msg['data']})


@socketio.on('connect', namespace='/chat')
def test_connect():
    print('connect llllla')
    # emit('connect', {'data': 'Connected'})
    send('connect')
    time.sleep(3)
    emit('connect', '123')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on_error_default
def default_error_handler(e):
    print(request.event["message"])  # "my error event"
    print(request.event["args"])


@socketio.on_error()
def error_handler(e):
    print(e)
