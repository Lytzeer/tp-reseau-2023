import socketserver
import http.server

PORT = 9999
HOST = '127.0.0.1'

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        #get and set http version from request
        self.protocol_version = self.request_version
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(b"\n\n<h1>Hello je suis un serveur HTTP</h1>")
    


with socketserver.TCPServer((HOST, PORT), MyHttpRequestHandler) as httpd:
    print("Server started at localhost:9999")
    httpd.serve_forever()