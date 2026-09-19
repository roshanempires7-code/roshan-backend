from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/lead', methods=['POST'])
def receive_lead():
    data = request.json
    print("New Lead Received:", data)
    return jsonify({"success": True, "message": "Lead received successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=False)
