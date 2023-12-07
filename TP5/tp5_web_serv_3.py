import socketserver
import http.server

PORT = 9999
HOST = '127.0.0.1'

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
    
with socketserver.TCPServer((HOST, PORT), MyHttpRequestHandler) as httpd:
    print("Server started at localhost:9999")
    httpd.serve_forever()