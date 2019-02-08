from flask import jsonify, make_response,request, Blueprint
from app.api.v1.views import bash
from app.api.v1.models.models import PartiesModel




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