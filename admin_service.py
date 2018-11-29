from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/aud')
def get_audience():
    info = requests.get('http://audience-service')
    return jsonify(info.json())

@app.route('/client')
def get_client():
    info = requests.get('http://client-service',)
    return jsonify(info.json())

@app.route('/campaign')
def get_campaign():
    info = requests.get('http://campaign-service')
    return jsonify(info.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=85, debug=True)
