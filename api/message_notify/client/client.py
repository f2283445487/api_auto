import socket
import time


def connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.124.39", 9999))
    return client


while True:
    try:
        s1 = connection()
        while True:
            time.sleep(1)
            s1.send(b"xiaoshen2")
            data = s1.recv(1024)
            print(data.decode("utf8"))
    except Exception as e:
        print(e)
        continue
