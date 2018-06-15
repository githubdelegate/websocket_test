from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit, send
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@app.route('/')
def index():
    # return render_template('index.html')
    d = {'error': 0,'result':['zy', 'nj']}
    return jsonify(d)

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
    print(request.event["message"]) # "my error event"
    print(request.event["args"])

@socketio.on_error()
def error_handler(e):
    print(e)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')