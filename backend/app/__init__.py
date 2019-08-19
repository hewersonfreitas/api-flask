from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object('config')

mongoDB = MongoClient(app.config['MONGODB_URI'])


@app.route("/")
def index():
    return "Auth"


@app.route("/api/list/all")
def find_all():
    stores = mongoDB.api.store.find()
    return dumps(stores)


@app.route("/api/list/<id>")
def find_one(id):
    store = mongoDB.api.store.find_one({'_id': ObjectId(id)})
    return dumps(store)


@app.route("/api/find/store")
def find_store():
    data = request.json
    store = mongoDB.api.store.find_one(
        {'city': data['city'], 'state': data['state']})
    return dumps(store)


@app.route('/api/add/store', methods=['POST'])
def add_store():
    data = request.json
    store_exists = mongoDB.api.store.find_one({'code': data['code']})

    if store_exists:
        return dumps(store_exists)

    if(len(data) < 4):
        return jsonify({'error': 'number fields error'}), 400
    else:
        for idx, value in data.items():
            if not value:
                return jsonify({'error': 'field {} is empty'.format(idx)}), 500

    code = data['code']
    name = data['name']
    city = data['city']
    state = data['state']

    try:
        mongoDB.api.store.insert({
            'code': code, 'name': name,
            'city': city, 'state': state
        })
    except Exception as e:
        return jsonify(
            {
                "error":
                "error to delete item _id:{0} from error:{1}".format(
                    id, str(e))
            }
        )

    return jsonify({
        'code': code, 'name': name, 'city': city, 'state': state
    })


@app.route('/api/update/store/<id>', methods=['PUT'])
def update_store(id):
    data = request.json
    if(len(data) < 4):
        return jsonify({'error': 'number fields error'}), 400
    else:
        for idx, value in data.items():
            if not value:
                return jsonify({'error': 'field {} is empty'.format(idx)}), 500

    code = data['code']
    name = data['name']
    city = data['city']
    state = data['state']

    mongoDB.api.store.update_one({'_id': ObjectId(id)}, 
                                 {'$set': 
                                    {'code': code, 'name': name, 'city': city, 'state': state}
                                 })

    return jsonify({
        'code': code, 'name': name,
        'city': city, 'state': state
    }), 200


@app.route("/api/delete/store/<id>", methods=['DELETE'])
def delete_one(id):
    try:
        mongoDB.api.store.delete_one({'_id': ObjectId(id)})
    except Exception as e:
        return jsonify(
            {
                "error":
                "error to delete item _id:{0} from error:{1}".format(
                    id, str(e))
            }
        )
    return jsonify({"message": "successful delete item _id:{}".format(id)})


CORS(app)