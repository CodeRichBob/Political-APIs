from flask import jsonify, make_response,request, Blueprint
from app.api.v1.views import bash
from app.api.v1.models.models import PartiesModel

@bash.route("/parties", methods=["GET"])
def getparties():
    return make_response(jsonify({
        "status": 200,
        "data": PartiesModel.view_all_parties()
    }), 200)

@bash.route("/parties", methods=["POST"])
def postparty():
    data = request.get_json()
    try:
        type = data['type']
        name = data['name']
        id = data['id']
    except:
        return make_response(jsonify({
            "status": 400,
            "error": "Not all fields are provided, must have id, name and type"
        }), 400)
    newparty = PartiesModel(name, type,id)
    newparty.saveparty()

    return make_response(jsonify({
        "status": 201,
        "data": [{
            "type": type,
            "name": name,
            "id": id
        }]
    }), 201)



@bash.route("/parties/<int:party_id>")
def get_single_party(party_id):

    party = PartiesModel.get_specific_party(party_id)

    if party:
        return make_response(jsonify({
            "status": 200,
            "data": party
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "Party not found"
}), 404)

@bash.route("/parties",methods=['PATCH'])
def edit_party():
    data = request.get_json()
    try:
        type = data['type']
        name = data['name']
        id = data['id']
    except:
        return make_response(jsonify({
            "status": 400,
            "error": "Not all fields are provided, must have id, name and type"
        }), 400)
    newparty = PartiesModel(name, type,id)
    newparty.saveparty()

    return make_response(jsonify({
        "status": 201,
        "data": [{
            "type": type,
            "name": name,
            "id": id
        }]
    }), 201)