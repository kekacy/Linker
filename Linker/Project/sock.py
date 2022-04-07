from flask_socketio import SocketIO, emit
from Linker import app
from flask import Flask
import time


socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret string'
    register_extensions(app)
    return app


def register_extensions(app):
    socketio.init_app(app)


@socketio.on('request_for_response', namespace='/testnamespace')
def give_response(data):
    value = data.get('param')
    emit('response', {'code': '200', 'msg': 'start to process ...'})
    time.sleep(5)
    emit('response', {'code': '200', 'msg': 'processed'})


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5050)
