from flask import Flask
from api.api_check.controller import check_controller
from api.message_notify.server.server import Server
from api.api_check import *
import threading


app = Flask(__name__)
app.register_blueprint(check_controller)
ser = Server()
threading.Thread(target=ser.main_server).start()

if __name__ == '__main__':
    app.run(host="192.168.124.39", port=7777)
