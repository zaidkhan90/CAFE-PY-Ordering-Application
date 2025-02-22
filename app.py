from flask import Flask, request, jsonify
from flask_cors import CORS  # To allow frontend requests

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

# Menu items with prices
menu = {
    'coffee': 80,
    'Pizza': 150,
    'Burger': 90,
    'Hot choclate': 150,
}

bill = 0  # Initialize bill

@app.route("/order", methods=["POST"])
def order():
    global bill  # Use global variable
    data = request.get_json()  # Get item from frontend
    item = data.get("item")

    if item in menu:
        bill += menu[item]
        return jsonify({"message": f"{item} added!", "bill": bill})
    else:
        return jsonify({"message": "Item not available!", "bill": bill})

if __name__ == "__main__":
    app.run(debug=True)
