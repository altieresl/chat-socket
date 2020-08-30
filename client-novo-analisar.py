# Chat - Script do servidor
# Autores: Altieres Luciano Pereira, Ângelo Matheus Pinto Savioti
# 2020/1
# Descricao: Nossa aplicação de chat permite que vários usuários se comuniquem ao mesmo tempo, além disso, todos os clientes recebem as mensagens enviadas por um cliente.
import socket
import sys
import threading

host = '191.252.186.52' # O ip 191.252.186.52 pode ser utilizado para testes pois é um servidor nosso onde o script se encontra rodando
porta = 50001
objSocket = None

def lerMensagens():
    while True:
        data = objSocket.recv(1024)
        print(data.decode())

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as objSocket: # Abre uma conexão tcp, utilizando ipv4, 
        objSocket.connect((host, porta)) # Se conecta ao ip e porta passados
        threadLerMensagens = threading.Thread(target=lerMensagens) # Cria uma thread para ficar recebendo as mensagens, é necessário fazer isso para que o programa continue recebendo as mensagens enquanto o usuário pode digitar por meio do input
        threadLerMensagens.daemon = True
        threadLerMensagens.start()
        while True:
            objSocket.sendall(input().encode()) # Envia o texto vindo do input
except Exception as e:
    print(e)
    objSocket.close()