import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        header = conn.recv(4)
        if not header: break

        msg_length = int.from_bytes(header[0:4], byteorder='big')

        print(f"Taille du message : {msg_length}")

        chunks = []

        bytes_recd = 0

        while bytes_recd < msg_length:
            chunks.append(conn.recv(1))

            if not chunks:
                raise RuntimeError("Socket connection broken")

            bytes_recd += len(chunks[-1])

        firstNumber = int.from_bytes(chunks[0], byteorder='big')
        operator = int.from_bytes(chunks[1], byteorder='big')
        convertedOperator = '+' if operator == 1 else '-' if operator == 10 else '*'
        secondNumber = int.from_bytes(chunks[2], byteorder='big')

        print(f"Calcul reÃ§u : {firstNumber} {convertedOperator} {secondNumber}")

        res  = eval(str(firstNumber) + convertedOperator + str(secondNumber))
        conn.send(str(res).encode())

    except socket.error:
        print("Error Occured.")
        break

conn.close()
s.close()