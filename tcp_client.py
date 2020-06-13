import socket


def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent = totalsent + sent

with open('text.pdf', 'rb') as f:
    filetosend = f.read()
    lenfile = len(filetosend)
    lenfilebytes = lenfile.to_bytes(lenfile.bit_length() + 7 // 8, 'big')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('192.168.0.102', 1234))
#s.connect(('127.0.0.1', 1234))
s.connect(('109.63.182.181', 27016))

s.sendall(lenfilebytes)
rsp = s.recv(1024)
mysend(s, filetosend)
s.close()
# changes for commit 2
