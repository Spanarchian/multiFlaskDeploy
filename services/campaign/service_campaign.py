from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
from py2neo import Graph
import os

# Instantiate the app
app = Flask(__name__)
api = Api(app)
# set up gdb & Env
load_dotenv(".env")
gdb = ""
ns = os.getenv('New_Name')

class Observatory(Resource):
    def get(self):

        return {
            'Campaign_Targets': ['Milkyway', 'Andromeda',
            'Large Magellanic Cloud (LMC)', ns]
        }

# Create routes
api.add_resource(Observatory, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)