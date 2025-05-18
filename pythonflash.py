from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! Deploy realizado com sucesso!"

if __name__ == '__main__':
    app.run()
