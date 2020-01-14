import socket
import time

HOST = ""
PORT = 8001
BUFFER = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsocket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while():
            conn, addr = s.accept()
            print("Connected by", addr)
            fullData = conn.recv(BUFFER)
            time.sleep(0.5)
            conn.sendall(fullData)
            conn.close

if __name__ == "__main__":
    main() 