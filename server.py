#!/usr/bin/env python

import sys, os, BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import config

# Change directory to serve:
BASEPATH = os.getcwd()
web_dir = os.path.join(BASEPATH, config.DIRECTORY)
os.chdir(web_dir)

if config.SSL:
	# SSL version taken from <https://gist.github.com/dergachev/7028596>
	# Generate "server.pem" file with:
	#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
	import ssl

	handler = SimpleHTTPRequestHandler
	handler.protocol_version = config.HTTP_PROTOCOL
	httpd = BaseHTTPServer.HTTPServer((config.SSL_HOST, config.SSL_PORT), handler)
	httpd.socket = ssl.wrap_socket(httpd.socket, certfile=os.path.join(BASEPATH, config.SSL_CERTFILE), server_side=True)
else:
	handler = SimpleHTTPRequestHandler
	handler.protocol_version = config.HTTP_PROTOCOL
	httpd = BaseHTTPServer.HTTPServer((config.HOST, config.PORT), handler)

# Initialize Server
sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()