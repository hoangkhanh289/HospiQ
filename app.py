from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(app="HospiQ", status="ok")

@app.get("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # dev server: chạy local port 5000
    app.run(host="0.0.0.0", port=5000)

