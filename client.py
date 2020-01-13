import socket

HOST = "www.google.com'"
PORT = 80

REQUEST = b"GET / HTTP/1.0\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.close()