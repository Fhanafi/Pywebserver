import http.server
import socketserver
PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Server berjalan di port", PORT)
    
    httpd.serve_forever()
