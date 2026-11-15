from http.server import HTTPServer, SimpleHTTPRequestHandler
from ssl import SSLContext, PROTOCOL_TLS_SERVER

context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain('localhost.pem')
httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket,server_side=True)
print('running server !!')
httpd.serve_forever()