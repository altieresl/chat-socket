import socket
import sys

#endereço broadcast para o qual os dados vão ser enviados
host = 'localhost'

#número da porta que o servidor que vai receber os dados está escutando
port = 50001

#cria um UDP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Envie para todo mundo
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)           
	
print ('Para sair use CTRL+X e pressione enter\n')
msg = input().encode()

while msg != '\x18':
	#envia os dados
	s.sendto(msg, (host, port))
	
	msg = input().encode()
	
print('closing socket')
s.close()