import socketserver
import http.server
import os
import logging

PORT = 9999
HOST = '127.0.0.1'

if not os.path.exists('./TP5/log/web_server'):
    os.makedirs('./TP5/log/web_server')


logging.basicConfig(filename='./TP5/log/web_server/web_server.log', level=logging.DEBUG)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.protocol_version = "HTTP/1.1"
        self.end_headers()

        if self.path == '/index.html':
            file = open('./TP5/index.html')
            content = file.read()
            file.close()
            self.wfile.write(content.encode())
        
        logging.info(f"GET request,\nPath: {str(self.path)}\nHeaders:\n{str(self.headers)}\n")
    
with socketserver.TCPServer((HOST, PORT), MyHttpRequestHandler) as httpd:
    print("Server started at localhost:9999")
    httpd.serve_forever()