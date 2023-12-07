import http.client

PORT = 9999
HOST = '127.0.0.1'

conn = http.client.HTTPConnection(HOST, PORT)

conn.request("GET", "/index.html")

awnser = conn.getresponse()

print(f"Status : {awnser.status} {awnser.reason}")
print(f"Header : {awnser.getheaders()}")
print(awnser.read().decode())

conn.close()