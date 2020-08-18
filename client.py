import socket
HOST = '191.252.186.52'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = input().encode()
while msg != '\x18':
    tcp.send (msg)
    msg = input().encode()
tcp.close()