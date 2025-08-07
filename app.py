import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI from the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/ip')
def get_ip():
    # We use request.remote_addr to get the client's IP address.
    # If the app is behind a proxy, this might not be the true client IP.
    # In a production environment, we would need to handle X-Forwarded-For headers.
    ip_address = request.remote_addr
    return jsonify({'ip': ip_address})

@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name} for user in users])

@app.route('/users/add')
def add_user():
    name = request.args.get('name')
    if name:
        try:
            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': f'User {name} added.'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Error adding user: {e}'})
    return jsonify({'message': 'Please provide a name.'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
