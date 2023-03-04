from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# bank1234
client = MongoClient(
    'mongodb://localhost:27017')
db = client['bank']
collection = db['banks']


# Get all banks
@app.route('/banks/', methods=['GET'])
def get_banks():
    bank = []
    for i in collection.find():
        i.pop('_id')
        name = i["bank_name"].replace(" ", "").lower()
        bank.append(name)
    unique_banks = list(set(bank))
    return jsonify(unique_banks)


@app.route('/banks/<string:bank_name>/', methods=['GET'])
def get_bank(bank_name):
    bank = []
    print(bank_name)
    for i in collection.find():
        i.pop('_id')
        if (i["bank_name"].replace(" ", "").lower() == bank_name.replace(" ", "").lower()):
            bank.append(i)
    return jsonify(len(bank), bank)


@app.route('/banks/<string:bank_name>/<string:branch>/', methods=['GET'])
def get_branch(bank_name, branch):
    bank = []
    print(bank_name)
    for i in collection.find():
        i.pop('_id')
        if (i["bank_name"].replace(" ", "").lower() == bank_name.replace(" ", "").lower() and i["branch"].replace(" ", "").lower() == branch.replace(" ", "").lower()):
            bank.append(i)
    return jsonify(len(bank), bank)


if __name__ == '__main__':
    app.run(debug=True)
