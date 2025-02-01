import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")


result = proxy.add
print("Result:", result)

result = proxy.add(4, 5)
print("Result:", result)

result = proxy.add(4, -5)
print("Result:", result)

try:
    result = proxy.add(4, -5, 6)
    print("Result:", result)
except xmlrpc.client.Fault as ex:
    print('xml rpc error', ex)
except Exception as ex:
    print(ex)
