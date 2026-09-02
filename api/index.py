import os
from datetime import timedelta

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY",
    "dev-secret-key-change-me-please-use-a-strong-secret-for-vercel",
)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=3)

jwt = JWTManager(app)


@app.get("/health")
def health():
    return jsonify({ "status": "ok", "routes": [ "/health", "/login", "/protected" ] }), 200


@app.route("/login", methods=["POST"])
def login():
    username = request.headers.get("username")
    password= request.headers.get("password")

    if username != "santhoshi@gmail.com" or password != "1234567890":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route("/protected", methods=["POST"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run(debug=True)


# In Postman: add the header Authorization with value "Bearer <access_token>"
