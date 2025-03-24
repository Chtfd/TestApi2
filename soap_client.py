from zeep import Client

client = Client('http://localhost:8000/?wsdl')

# Ambil Contact
response = client.service.GetContact(1)
print(response)

# Ambil Address
response = client.service.GetAddress(1)
print(response)
