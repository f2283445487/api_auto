import socket, threading
import time
from . import result_message_notify
from queue import Queue


class Server(object):
    def __init__(self):
        self.bind_ip = "127.0.0.1"  # ip
        self.bind_port = 9999  # port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.bind_ip, self.bind_port))
        self.server.listen(5)
        self.user_map = {}
        print("start")

    def server_login(self):
        while True:
            client, addr = self.server.accept()
            request_data = client.recv(1024).decode("utf8")
            self.user_map[request_data] = client
            result_message_notify[request_data] = Queue()
            print(request_data)
            client.send(("hello: " + request_data).encode("utf8"))

    def tcp_link(self):
        # client.send(b'Welcome!')
        while True:
            if result_message_notify:
                for message_user in result_message_notify:
                    try:
                        client = self.user_map.get(message_user)
                        if client and (not result_message_notify[message_user].empty()):
                            client.send(result_message_notify[message_user].get().encode("utf8"))
                        else:
                            continue
                    except Exception as e:
                        self.user_map.pop(message_user)
                        print(e)
            time.sleep(1)

    def main_server(self):
        threading.Thread(target=self.server_login).start()
        self.tcp_link()


# ser = Server()
# threading.Thread(target=ser.main_server).start()

if __name__ == '__main__':
    pass
