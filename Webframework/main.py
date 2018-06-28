from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import requests
import random
import urllib

routes = {}
lines = []

def render_template(template):
    code = ""
    with open("templates\\{0}".format(template)) as f:
        code = f.read()
    return code

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.wfile.write(routes[self.path].encode())
        except KeyError:
            if not self.path in routes:
                self.send_response(404)
                self.wfile.write("<h1>404 Conda can't find this page!</h1>".encode())
        except ConnectionResetError:
            pass

class Server(ThreadingMixIn, HTTPServer):
    pass    

class WebConda():
    def __init__(self,moduleName,host="127.0.0.1",port=5000):
        self.address = (host, port)
        self.SERVER = Server(self.address, RequestHandler)

    def route(self,f, route):
        routes[route] = f()

    def run(self):
        try:
            print("Server started:")
            self.SERVER.serve_forever()
        except KeyboardInterrupt:
            print("Admin has shutdown the Server!")