from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "Secure CI/CD Pipeline",
        "message": "Welcome to our DevSecOps project!",
        "developer": "Ahsan",
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "application": "Secure CI/CD Pipeline",
        "status": "healthy"
    }), 200


@app.route("/api/users", methods=["GET"])
def get_users():

    users = [
        {
            "id": 1,
            "name": "Ahsan",
            "role": "DevOps Engineer"
        },
        {
            "id": 2,
            "name": "Ali",
            "role": "Developer"
        },
        {
            "id": 3,
            "name": "Arbaz",
            "role": "Security Engineer"
        }
    ]

    return jsonify({
        "users": users,
        "total": len(users)
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
