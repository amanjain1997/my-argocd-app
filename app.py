from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from ArgoCD! Aman"  # Or use Amisha — your choice

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
