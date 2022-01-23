from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
TCPServer(("",8080), SimpleHTTPRequestHandler).serve_forever()