from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.environ.get('APP_VERSION', '1.0')
    return jsonify({"message": "CKAD GitOps App rodando liso na OCI!", "version": version})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)