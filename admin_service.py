from flask import Flask, jsonify
import requests
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    info = requests.get('http://client-service')
    return jsonify(info.json())


@app.route('/campaign')
def get_campaign():
    logger.info('Start get_campaign')
    info = requests.get('http://campaign-service')
    print("get_campaign() RTND -: - {}".format(info.json()))
    return jsonify(info.json())


@app.route('/campaign/ref/<id_ref>')
def get_campaign_by_ref(id_ref):
    logger.info('Start get_campaign_by_ref')
    info = requests.get('http://campaign-service/ref/'+id_ref)
    print("get_campaign_by_ref() RTND -: - {}".format(info.json()))
    return jsonify(info.json())


@app.route('/campaign/ind/<id_ref>')
def get_campaign_by_industry(id_ref):
    logger.info('Start get_campaign_by_industry')
    info = requests.get('http://campaign-service/ind/'+id_ref)
    logger.info("get_campaign_by_industry() RTND -: - {}".format(info.json()))
    return jsonify(info.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=85, debug=True)
