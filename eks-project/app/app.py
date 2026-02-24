
from flask import Flask, jsonify
import socket

app = Flask(__name__)
@app.route("/", methods=["GET"])
def get_my_ip():
   return jsonify(socket.gethostbyname(socket.gethostname())), 200

app.run(host="0.0.0.0", port=5000, debug=True)
