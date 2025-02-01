import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
#print(dir(proxy))


response = proxy.hello()
print(f"{response =}")