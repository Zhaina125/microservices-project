from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def get_users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Aigerim"},
            {"id": 2, "name": "Nursultan"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
