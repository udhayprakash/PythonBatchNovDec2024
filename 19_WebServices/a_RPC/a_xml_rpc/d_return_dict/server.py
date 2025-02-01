from xmlrpc.server import SimpleXMLRPCServer


DOZEN = 12

def get_info():
    return {"name": "John", "age": 30, "occupation": "Engineer"}


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(get_info, "info")
server.register_function(DOZEN, "dozen")

server.serve_forever()