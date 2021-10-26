from os import name
from flask_socketio import SocketIO
from flask import Flask,render_template,request

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('cvdata',namespace='/cv')
def handle_cv_message(message):
    print("sending to server2web")
    # print(message.image)
    socketio.emit('toclient', {'image': message['image']},namespace="/web")

# @socketio.on('connect')
# def connect_web():
#     # print("connected")
#     # socketio.emit('my response', {'data': 'Connected'})
#     print('[INFO] Web Client connected: {}'.format(request.sid))

@socketio.on('connect',namespace='/web')
def connect_web():
    print("connected")
    print('[INFO] Web Client connected: {}'.format(request.sid))

@socketio.on('disconnect',namespace='/web')
def disconnet_web():
    print('[INFO] Web Client disconnected: {}'.format(request.sid))

@socketio.on('connect', namespace='/cv')
def connect_cv():
    print('[INFO] CV client connected: {}'.format(request.sid))


@socketio.on('disconnect', namespace='/cv')
def disconnect_cv():
    print('[INFO] CV client disconnected: {}'.format(request.sid))



if __name__ == "__main__":
    print("[INFO] Starting server at https://localhost:5001")
    socketio.run(app=app,host='0.0.0.0', port=5001)