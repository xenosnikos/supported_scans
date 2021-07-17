from flask import Flask
from flask_restful import Api

from controllers import scans_available

app = Flask(__name__)
api = Api(app)

api.add_resource(scans_available.AvailableScans, '/v2/supportedScans')

if __name__ == "__main__":
    app.run()
