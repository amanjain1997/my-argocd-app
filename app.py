from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
    return "Hello from ArgoCD! Aman"
=======
    return "Hello from ArgoCD! Amisha"
>>>>>>> 28db487 (WIP: saving changes before pulling)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

