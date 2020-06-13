import socket


def myreceive(sock, msglen):
    msg = b''
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        if chunk == '':
            raise RuntimeError('broken')
        msg = msg + chunk
    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.101', 1234))
#s.bind(('127.0.0.1', 1234))
s.listen(1)
conn, addr = s.accept()

data = conn.recv(1024)
msglen = int.from_bytes(data, 'big')
conn.sendall(b'ready')
with open('package.zip', 'wb') as f:
    f.write(myreceive(conn, msglen))
conn.close()

