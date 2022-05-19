# -*- coding: utf-8 -*-
import socket
import threading
host = '127.0.0.1'
port = 2000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

print("Start Job")
def broadcast(message):
    for client in clients:  # Метод отправки всем клиентам
        if(clientes != client): # Проверка на себя
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)     # Получение сообщения
            broadcast(message)  # Вызов метода для отпраки сообщения
        except:
            index = clients.index(client)   # Взятие индекса клиента отправившего сообщения
            clients.remove(client)  #Удаление из списка клиентов этого клиента
            client.close()  # Закрытие соединения с клиентом
            nickname = nicknames[index]     # Взятие никнейма из списка ников
            nicknames.remove(nickname)  # Удаление из списка ников
            break   # Стоп

def receive():
    while True:
        client, address = server.accept()   # Подключение клиента
        print(format(str(address)))     # Вывод кликента в консоль
        nickname = client.recv(1024).decode('utf-8')    # Сохранение ника в переменную
        nicknames.append(nickname)  # Добавление в списки ников
        clients.append(client)  # Добавление в списки клиентов
        print(format(nickname)) # Вывод нового ника
        thread = threading.Thread(target=handle, args=(client,))    # Запуск многопоточности
        thread.start() # Старт многопоточности

receive()