import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

HOSTS = json.load(open('settings.json'))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        for s in HOSTS :
            try:
                stream = os.popen('ping -c 3 ' + s['ip'])
                output = stream.read()
                self.wfile.write((str(s) + "\n\n").encode())
                self.wfile.write(output.encode())
                self.wfile.write('----------------------------------\n\n'.encode())
            except Exception as e:
                print(e)


httpd = HTTPServer(('', int(sys.argv[1])), SimpleHTTPRequestHandler)
httpd.serve_forever()
