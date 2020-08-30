import socket
import sys
import threading
host = '191.252.186.52'
porta = 50001
objSocket = None

def lerMensagens():
    while True:
        data = objSocket.recv(1024)
        print(data.decode())

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as objSocket:
        objSocket.connect((host, porta))
        threadLerMensagens = threading.Thread(target=lerMensagens)
        threadLerMensagens.daemon = True
        threadLerMensagens.start()
        while True:
            objSocket.sendall(input().encode())
except Exception as e:
    print(e)
    objSocket.close()