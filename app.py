from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Shows which Pod is answering the request
    pod_name = os.getenv('HOSTNAME', 'Unknown')
    return f"<h1>Hello from K3s!</h1><p>Served by Pod: {pod_name}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)