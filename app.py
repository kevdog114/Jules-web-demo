from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ip')
def get_ip():
    # We use request.remote_addr to get the client's IP address.
    # If the app is behind a proxy, this might not be the true client IP.
    # In a production environment, we would need to handle X-Forwarded-For headers.
    ip_address = request.remote_addr
    return jsonify({'ip': ip_address})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
