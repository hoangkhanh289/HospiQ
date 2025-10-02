from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(app="HospiQ", status="ok")


@app.get("/health")
def health():
    return "OK", 200


# API mới
@app.get("/get_number")
def get_number():
    # Lấy id từ query param: /get_number?id=123
    user_id = request.args.get("id", type=int)

    if user_id is None:
        return jsonify(error="Missing id"), 400

    # Giả sử bạn muốn map id thành số thứ tự và tên
    # Ở đây làm demo: id -> stt = id, tên = "User <id>"
    result = {"stt": user_id, "ten": f"User {user_id}"}
    return jsonify(result)


if __name__ == "__main__":
    # dev server: chạy local port 5000
    app.run(host="0.0.0.0", port=5000)
