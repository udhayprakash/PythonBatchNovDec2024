import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
result = proxy.info()

print("Name:", result["name"])
print("Age:", result["age"])
print("Occupation:", result["occupation"])

print(f'{proxy.dozen =}')
# print(f'{proxy.dozen() =}')
# constant cant be exposed directly 
