import wsgiref.simple_server


def application(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


server = wsgiref.simple_server.make_server('', 9090, application)
print('running..')
server.serve_forever()
