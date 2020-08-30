# Chat - Script do servidor
# Autores: Altieres Luciano Pereira, Ângelo Matheus Pinto Savioti
# 2020/1
# Descricao: Nossa aplicação de chat permite que vários usuários se comuniquem ao mesmo tempo, além disso, todos os clientes recebem as mensagens enviadas por um cliente.
import socket
import os
from threading import Thread
import threading

clients = set() # Lista de clientes que será utilizada para enviar cada mensagem a todos os clientes conectados
clients_lock = threading.Lock() # Lock da thread

def listener(client, address):
    print ("Conexão iniciada com o IP: ", address)
    with clients_lock: # Utilizado o lock da thread para criar uma "seção crítica", garantindo que apenas uma thread por vez estará rodando o codigo dentro desse bloco
        clients.add(client)
    try:    
        while True:
            data = client.recv(1024) # Lê até 1024 bytes recebidos pelo socket
            if not data:
                break
            else:
                print (repr(data))
                with clients_lock: # Utilizado o lock da thread para criar uma "seção crítica", garantindo que apenas uma thread por vez estará rodando o codigo dentro desse bloco
                    for c in clients: # Envia a mensagem a todos os clientes
                        c.sendall(address[0] + " diz: " + data)
    finally:
        with clients_lock: # Utilizado o lock da thread para criar uma "seção crítica", garantindo que apenas uma thread por vez estará rodando o codigo dentro desse bloco
            clients.remove(client) # Quando o cliente encerra a conexão, remove ele da lista de clientes
            client.close() # Fecha a conexão com ele

host = ''
port = 50001
print('aaa')

try:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # A Flag SO_REUSEADDR serve para fazer com que o kernel possa reutilizar um endereço sem ter que esperar seu timeout (geralmente esse problema ocorre ao fechar o servidor e depois tentar abrir em seguida)

    s.bind((host,port)) # Seta o ip e a porta do servidor, no caso o ip está vazio pois é o localhost
    s.listen(5)
    threads = []

    while True:
        print ("Aguardando conexões")
        client, address = s.accept() # Quando uma conexão é recebida o software aceita e cria uma thread que ficará esperando as mensagens
        threads.append(Thread(target=listener, args = (client,address)).start())

    s.close()
except Exception as e:
    print(e)
    s.close()