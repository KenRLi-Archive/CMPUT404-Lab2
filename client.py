import socket
import sys

def createTCPSocket():
    print("Creating Socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f"Failed to create socket. Error code: {str(msg[0])}, Error message: {msg[1]}")
        sys.exit()
    print("Socket Created Successfully")
    return s

def getRemoteIP(host):
    print(f"Getting IP for {host}")
    try:
        remoteIP = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit()
    print(f"IP address of {host} is {remoteIP}")
    return remoteIP

def sendData(serverSocket, payload):
    print("Sending Payload")
    try:
        serverSocket.sendall(payload.encode())
    except socket.error:
        print("Send Failed")
        sys.exit()
    print("Payload sent successfully")

def main():
    try:
        HOST = "www.google.com"
        PORT = 80
        PAYLOAD = b"GET / HTTP/1.0\r\nHost: " + HOST + "\r\n\r\n"
        BUFFER_SIZE = 4096

        s = createTCPSocket()

        remoteIP = getRemoteIP(HOST)

        s.connect((remoteIP, PORT))

        sendData(s, PAYLOAD)
        s.shutdown(socket.SHUT_WR)

        # fullData = b""
        while():
            data = s.recv(BUFFER_SIZE)

            if not data:
                break
            
            print("> Sockets - Step 2")
            print(data)
    except Exception as e:
        print(e)
    # finally:
    #     s.close()

if __name__ == "__main__":
    main()