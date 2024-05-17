from spyne import Application, rpc, ServiceBase, \
    Iterable, Unicode, ComplexModel, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from google.cloud import firestore

db = firestore.Client()

class Product(ComplexModel):
    id = String
    name = String
    price = String

class ProductService(ServiceBase):
    @rpc(_returns=Iterable(Product))
    def get_products(ctx):
        products_ref = db.collection(u'products')
        docs = products_ref.stream()
        products = []
        for doc in docs:
            print(doc)
            doc_dict = doc.to_dict()
            products.append(Product(id=doc_dict['id'], name=doc_dict['name'], price=doc_dict['price']))
        return products

    @rpc(Product, _returns=Product)
    def post_product(ctx, product):
        db.collection(u'products').add({
            'id': product.id,
            'name': product.name,
            'price': product.price
        })
        return product

application = Application([ProductService],
    tns='spyne.examples.products',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8080, wsgi_app)
    print("listening to http://0.0.0.0:8080")
    print("wsdl is at: http://0.0.0.0:8080/?wsdl")
    server.serve_forever()