from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello My Name is Bhajan And this is my first live application."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
 