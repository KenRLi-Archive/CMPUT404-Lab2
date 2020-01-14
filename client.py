import socket

HOST = "www.google.com"
PORT = 80
PAYLOAD = "GET / HTTP/1.0\r\nHost: " + HOST + "\r\n\r\n"
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(PAYLOAD.encode())

data = s.recv(BUFFER_SIZE) 
print(data)

s.close()