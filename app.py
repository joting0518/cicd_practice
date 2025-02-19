from flask import Flask, jsonfiy

app = Flask(__name__)

@app.route('/hello',method=['GET'])
def hello():
    return jsonfiy({"message": "hello world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
