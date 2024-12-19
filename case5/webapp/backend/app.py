from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Data dictionary
data = {
    'users': [
        {
            'name': 'Yono',
            'age': 25,
            'address': 'Jl. Merpati No. 1',
            'phone': '081234567890'
        },
        {
            'name': 'Ayu',
            'age': 30,
            'address': 'Jl. Kenari No. 5',
            'phone': '081298765432'
        },
        {
            'name': 'Budi',
            'age': 28,
            'address': 'Jl. Melati No. 10',
            'phone': '081376543210'
        }
    ]
}

@app.route('/')
def home():
    return "Backend is Running"

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)