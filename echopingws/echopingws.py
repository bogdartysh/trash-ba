import json, os
from http.server import HTTPServer, BaseHTTPRequestHandler

settings = json.load(open('settings.json'))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        isAllowed = False
        for a in self.client_address:
            if str(a) in settings["allowedips"] :
                isAllowed = True
        if isAllowed != True:
            self.send_response(403)
            self.wfile.write(str(self.client_address).encode())
            return
        self.send_response(200)
        self.end_headers()
        for s in settings['hosts'] :
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

