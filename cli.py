import requests

print("\n\nGroup 8 CLI\n--------------------------\n")

ip = input("Enter the address of API:")
port = input("Enter the port of API:")
dest = input("Enter destination of request:")
req = input("Enter request:")

address = ('http://' + ip + ':' + port + '/' + dest + '/' + req)

result = requests.get(address)
results_text = result.json()
print(results_text)
