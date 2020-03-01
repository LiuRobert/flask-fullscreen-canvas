from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def base():
    return send_from_directory("static", "index.html")

@app.route("/js/<file>")
def js(file):
    return send_from_directory("static/js", file, mimetype="text/javascript")

@app.route("/css/<file>")
def css(file):
    return send_from_directory("static/css", file, mimetype="text/css")


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=4200)