from flask import Flask, request, jsonify, abort
from google.cloud import firestore

app = Flask(__name__)

db = firestore.Client()

orders = [{"order:": "order1"}, {"order": "order2"}]

USERNAME = "apigeechallenge"
PASSWORD = "ApigeeChallenge2024"

@app.route('/orders', methods=['GET'])
def get_orders():
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        abort(401)
    orders_ref = db.collection(u'orders')
    docs = orders_ref.stream()
    orders = []
    for doc in docs:
        orders.append(doc.to_dict())
    print(orders)
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def post_order():
    auth = request.authorization
    if not auth or auth.username != USERNAME or auth.password != PASSWORD:
        abort(401)
    order = request.get_json()
    # orders.append(order)
    db.collection(u'orders').add(order)
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)