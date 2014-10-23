from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run(host = '172.27.17.9', port = 8080)
    #app.run()
