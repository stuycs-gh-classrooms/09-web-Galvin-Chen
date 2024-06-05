#!/usr/bin/python
print('Content-type: text/html\n')
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('frontier.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/Dream1':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('dream1.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/Day1':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('page3.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/Dream1_start':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('page3.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/ending2':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>You ran away and lived to tell the tale.</h1>')
        elif self.path == '/ending3':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>You found the treasure chest and became rich!</h1>')
        elif self.path == '/ending4':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>You resisted the temptation and continued your journey.</h1>')
        elif self.path.endswith('.css'):
            css_path = self.path.lstrip('/')
            if os.path.exists(css_path):
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                with open(css_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'CSS file not found')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Page not found')

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

