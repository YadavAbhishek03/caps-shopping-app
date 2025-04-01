from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000
DIRECTORY = "static"

class RequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Override to serve files from the 'static' directory
        path = super().translate_path(path)
        if os.path.commonpath([path, os.path.abspath(DIRECTORY)]) == os.path.abspath(DIRECTORY):
            return os.path.join(DIRECTORY, os.path.relpath(path, os.path.abspath(DIRECTORY)))
        return path

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {PORT}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

