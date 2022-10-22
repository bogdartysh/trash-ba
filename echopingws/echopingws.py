import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
settings = json.load(open('settings.json'))
print ('Argument List:', settings)
HOSTS = settings['hosts']

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


httpd = HTTPServer((settings['binding'], int(settings['port'])), SimpleHTTPRequestHandler)
httpd.serve_forever()
