import socket
import sys
import threading
host = '191.252.186.52'
porta = 50002
objSocket = None

def lerMensagens():
    while True:
        data = objSocket.recv(1024)
        print(data.decode())

try:
    for res in socket.getaddrinfo(host, porta, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            objSocket = socket.socket(af, socktype, proto)
        except OSError as msg:
            objSocket = None
            continue
        try:
            objSocket.connect(sa)
        except OSError as msg:
            objSocket.close()
            objSocket = None
            continue
        break
    if objSocket is None:
        print('Erro ao abrir o socket')
        sys.exit(1)
    with objSocket:
        threadLerMensagens = threading.Thread(target=lerMensagens)
        threadLerMensagens.daemon = True
        threadLerMensagens.start()
        while True:
            objSocket.sendall(input().encode())
except:
    objSocket.close()