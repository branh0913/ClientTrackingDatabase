from flask.ext.restful import Resource, reqparse, Api
from Insert_Data.Data_Insert import ClientDataInsert

__author__ = 'Brandon'

from flask import Flask, render_template


app = Flask(__name__)

api = Api(app)

class ClientResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('priority')
    parser.add_argument('note')
    parser.add_argument('summaary')

    def get(self, priority, note, summary):

        client = ClientDataInsert()
        client.insert_data(priority=priority, note=note, summary=summary)


api.add_resource(ClientResource, '/Client/<string:priority>/<string:note>/<string:summary>/')




@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)




