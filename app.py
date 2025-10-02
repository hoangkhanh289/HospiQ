from flask import Flask, jsonify, request
from functools import wraps
import os

app = Flask(__name__)

# Lấy đường dẫn tới file api_key.txt nằm cùng thư mục với app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(BASE_DIR, "api_key.txt")


def load_api_key():
    """Đọc API key từ file, nếu chưa có thì tạo file mới."""
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "w") as f:
            f.write("DEFAULT_SECRET_KEY_123")
    with open(KEY_FILE, "r") as f:
        return f.read().strip()


def require_api_key(func):
    """Decorator kiểm tra API Key từ file"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = load_api_key()
        client_key = request.headers.get("X-API-KEY")
        if client_key != api_key:
            return jsonify(error="Unauthorized"), 401
        return func(*args, **kwargs)

    return wrapper


@app.get("/")
def home():
    return jsonify(app="HospiQ", status="ok")


@app.get("/health")
def health():
    return "OK", 200


@app.get("/get_number")
@require_api_key
def get_number():
    user_id = request.args.get("id", type=int)
    if user_id is None:
        return jsonify(error="Missing id"), 400

    result = {"stt": user_id, "ten": f"User {user_id}"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
