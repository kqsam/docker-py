from flask import Flask

app = Flask(__name__)


@app.route("/")
def run_index():
    return "<p>Hello, World!</p>"


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=("3000"),debug=True)

