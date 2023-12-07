import socket

HOST = '127.0.0.1'
PORT = 8888


def main():
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    sock.send("Hello".encode())

    data = sock.recv(1024)

    print(f"Received : {data.decode()}")

    sock.close()

if __name__ == "__main__":
    main()