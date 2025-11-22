from flask import Flask

app = Flask(__name__)

@app.route("/orders")
def orders():
    return {"orders": ["order-1", "order-2"]}

if __name__ == "__main__":
    app.run(port=5002)
