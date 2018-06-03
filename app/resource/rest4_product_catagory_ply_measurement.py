from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from app.helper.catchBlankString import catchEmptyString


resource_field= {
    "productCatMeasureID": fields.Integer,
    "productId": fields.Integer,
    "productCatId": fields.Integer,
    "plyPositionId": fields.Integer,
    "size": fields.Integer,
    "bf": fields.Integer,
    "gsm": fields.Integer,
    "shade": fields.Integer,
    "createdAt": fields.Integer,
    "updatedAt": fields.Integer
}

data = {"productCatMeasureID":1, "productId":1, "productCatId":1, \
    "plyPositionId":2, "size":10, "bf":11,   \
    "gsm": 10, "shade":4, "createdAt":1, \
        "updatedAt":0}

class ProductCatPlyMeasurement(Resource):
    @marshal_with(resource_field, envelope="data")
    def get(self):
        return data

    def post(self):
        parser = reqparse.RequestParser(bundle_errors= True)

        parser.add_argument("productCatMeasureID", required=True, type= int)
        parser.add_argument("productId", required= True, type= int)
        parser.add_argument("productCatId", required= True, type= int)
        parser.add_argument("size", required= True, type= int)
        parser.add_argument("gsm", required= True, type= int)
        parser.add_argument("shade", required= True, type= int)
        parser.add_argument("height", required= True, type= int)
        parser.add_argument("createdAt", required= True, type= int)
        parser.add_argument("updatedAt", required= True, type= int)


        args = parser.parse_args()

        return args
