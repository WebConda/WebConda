"""MIT License

Copyright (c) 2018 WebConda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

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