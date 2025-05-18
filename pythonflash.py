from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! Deploy realizado com sucesso!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
