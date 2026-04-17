from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<html><head><title>Hello Python App</title></head><body><h1>Hello Python App</h1></body></html>")

    def log_message(self, format, *args):
        return


if __name__ == '__main__':
    port = int(os.getenv('PORT', '8080'))
    server = HTTPServer(('0.0.0.0', port), HelloHandler)
    print(f'Serving on http://localhost:{port}')
    server.serve_forever()
