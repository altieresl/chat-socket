import socket
import sys
from aioconsole import ainput
import asyncio
HOST = '191.252.186.52'
PORT = 50000              # The same port as used by the server

async def lerMensagens():
    
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    while True:
        entrada = input('Is this your line? ').encode()
        s.sendall(entrada)
        data = s.recv(1024)
        rint('Received', repr(data))
