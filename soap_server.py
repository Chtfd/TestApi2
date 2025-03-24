from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class ContactAddressService(ServiceBase):
    contacts = {
        1: {"first_name": "Chaterina", "last_name": "Fatma", "email": "Chaterina@example.com", "phone": "123456789"}
    }
    addresses = {
        1: {"street": "jl A.yani 07", "city": "Surabaya", "province": "Jawa Timur", "country": "Indonesia", "postal_code": "10110"}
    }

    @rpc(Integer, _returns=Unicode)
    def GetContact(ctx, contactId):
        contact = ContactAddressService.contacts.get(contactId, {})
        return f"Name: {contact.get('first_name')} {contact.get('last_name')}, Email: {contact.get('email')}, Phone: {contact.get('phone')}"

    @rpc(Integer, _returns=Unicode)
    def GetAddress(ctx, addressId):
        address = ContactAddressService.addresses.get(addressId, {})
        return f"Street: {address.get('street')}, City: {address.get('city')}, Province: {address.get('province')}, Country: {address.get('country')}, Postal Code: {address.get('postal_code')}"

application = Application([ContactAddressService],
    tns="http://example.com/contactaddress",
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server running on port 8000...")
    server.serve_forever()
