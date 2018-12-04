from flask import Flask, jsonify
from flask_restful import Resource, Api
from dotenv import load_dotenv
from py2neo import Graph
from data_collector import get_all, get_by_id, get_by_industry
import os

# Instantiate the app
app = Flask(__name__)
api = Api(app)
# set up gdb & Env
load_dotenv(".env")
gdb = ""
ns = os.getenv('New_Name')


class Campaign(Resource):
    def get(self):
        data = get_all()
        return data


class CampaignByRef(Resource):
    def get(self, id_ref):
        data = get_by_id(id_ref)
        return data

class CampaignByInd(Resource):
    def get(self, id_ref):
        data = get_by_industry(id_ref)
        return data

# Create routes
api.add_resource(Campaign, '/')
api.add_resource(CampaignByRef, '/ref/<id_ref>')
api.add_resource(CampaignByInd, '/ind/<id_ref>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)