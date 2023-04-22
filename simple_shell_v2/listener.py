import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('localhost', 8080))
listener.listen()
print('server started')
connection, address = listener.accept()
print(f'got connection from {address}')


def recv_data():
    original_size = connection.recv(2048).decode('utf-8')
    original_size = int(original_size)
    data = connection.recv(2048)
    while len(data) != original_size:
        data += connection.recv(2048)
    return data


while True:
    cmd = input('Enter a cmd: ')
    if cmd == 'quit':
        connection.send(b'quit')
        connection.close()
        break
    elif cmd[:2] == 'cd':
        connection.send(bytes(cmd, 'utf-8'))
        continue
    connection.send(bytes(cmd, 'utf-8'))
    recv_data = connection.recv(2048)
    print(recv_data.decode('utf-8'))


