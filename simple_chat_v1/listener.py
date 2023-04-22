import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('localhost', 8080))
listener.listen()
print('server started')
connection, address = listener.accept()
print(f'got connection from {address}')

while True:
    chat = input('>> ')
    connection.send(bytes(chat, 'utf-8'))
    recv_data = connection.recv(2048)
    print(recv_data.decode('utf-8'))


