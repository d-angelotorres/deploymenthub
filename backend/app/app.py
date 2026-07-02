from flask import Flask, jsonify

app = Flask(__name__)

servers = [
    {
        "id": 1,
        "hostname": "web-01",
        "environment": "Production",
        "status": "Online",
        "ip": "10.0.0.15"
    },
    {
        "id": 2,
        "hostname": "db-01",
        "environment": "Production",
        "status": "Online",
        "ip": "10.0.0.20"
    },
    {
        "id": 3,
        "hostname": "dev-01",
        "environment": "Development",
        "status": "Offline",
        "ip": "10.0.1.10"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "DeploymentHub API is running!"
    })


@app.route("/servers")
def get_servers():
    return jsonify(servers)


if __name__ == "__main__":
    app.run(debug=True)