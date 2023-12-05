from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('kull.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
    app.run()




