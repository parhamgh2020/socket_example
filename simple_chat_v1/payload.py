import socket

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
payload.connect(('localhost', 8080))
print('establish connect')

while True:
    recieve_data = payload.recv(2048)
    print(recieve_data.decode('utf-8'))
    chat = input('>> ')
    payload.send(bytes(chat, 'utf-8'))
