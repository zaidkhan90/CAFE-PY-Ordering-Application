from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "cafe_py_secret_key"
CORS(app)

menu = {
    "Coffee": 80,
    "Pizza": 150,
    "Burger": 90,
    "Hot Chocolate": 150
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-item", methods=["POST"])
def add_item():
    item = request.json["item"]
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append({"name": item, "price": menu[item]})
    session.modified = True
    return jsonify({"message": f"{item} added to cart", "cart": session["cart"]})

@app.route("/clear-cart", methods=["POST"])
def clear_cart():
    session.pop("cart", None)
    return jsonify({"message": "Cart cleared"})

@app.route("/get-total", methods=["GET"])
def get_total():
    total = sum(item["price"] for item in session.get("cart", []))
    return jsonify({"total": total})

if __name__ == "__main__":
    app.run(debug=True)
