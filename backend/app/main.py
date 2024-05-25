from flask import Flask, jsonify, request

from services import rating_service, order_history_service, payment_service

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, I am alive!'

# get order history
@app.route('/api/orderHistory', methods=['GET'])
def get_order_history_service():
    data = order_history_service.get_order_history_service(request.get_json())#
    return jsonify(data)

# get rating
@app.route('/api/getRating', methods=['GET'])
def get_rating():
    data = rating_service.get_rating_service(request.get_json())#
    return jsonify(data)

# update rating
@app.route('/api/updateRating', methods=['POST'])
def update_rating():
    data = rating_service.update_rating_service(request.get_json())#
    return jsonify(data)

# payment notification
@app.route('/api/paymentNotification', methods=['GET'])
def payment_notiy():
    data = payment_service.payment_notification_service(request.get_json())#
    return jsonify(data)

@app.route('/api/payment', methods=['POST'])
def payment():
    data = payment_service.payment(request.get_json())
    return jsonify(data)

# test
@app.route('/api/test', methods=['GET'])
def test():
    data = order_history_service.test()#
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
