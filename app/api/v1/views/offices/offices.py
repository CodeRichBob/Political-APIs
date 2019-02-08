from flask import jsonify, make_response,request, Blueprint
from app.api.v1.views import views
from app.api.v1.models.models import OfficesModel

@views.route("/getoffice")
def getoffice():
    return "jjustanoffice"
    
@views.route("/offices", methods=["GET"])
def getoffices():
    return make_response(jsonify({
        "status": 200,
        "data": OfficesModel.view_all_offices()
    }), 200)

@views.route("/offices", methods=["POST"])
def postoffice():
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
    newoffice = OfficesModel(name, type,id)
    newoffice.saveoffice()

    return make_response(jsonify({
        "status": 201,
        "data": [{
            "type": type,
            "name": name,
            "id": id
        }]
    }), 201)



@views.route("/offices/<int:office_id>")
def get_single_office(office_id):

    office = OfficesModel.get_specific_office(office_id)

    if office:
        return make_response(jsonify({
            "status": 200,
            "data": office
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "Office not found"
}), 404)