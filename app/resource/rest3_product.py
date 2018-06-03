from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from app.helper.catchBlankString import catchEmptyString

resource_field= {
    "productId": fields.Integer,
    "productCatId": fields.Integer,
    "measureUniId": fields.Integer,
    "productName": fields.String,
    "length": fields.Integer,
    "breadth": fields.Integer,
    "height": fields.Integer,
    "createdAt": fields.Integer,
    "updatedAt": fields.Integer
}

data = {"productId":1, "productCatId":1, "measureUniId":1, \
    "productName":"Carton Box", "length":10, "breadth":11,   \
    "height": 10, "createdAt":1, \
        "updatedAt":0}

class plyPosition(Resource):
    @marshal_with(resource_field, envelope="data")
    def get(self):
        return data

    def post(self):
        parser = reqparse.RequestParser(bundle_errors= True)

        parser.add_argument("productId", required=True, type= int)
        parser.add_argument("productCatId", required= True, type= int)
        parser.add_argument("measureUniId", required= True, type= int)
        parser.add_argument("productName", required= True, type= str)
        parser.add_argument("length", required= True, type= int)
        parser.add_argument("breadth", required= True, type= int)
        parser.add_argument("height", required= True, type= int)
        parser.add_argument("createdAt", required= True, type= int)
        parser.add_argument("updatedAt", required= True, type= int)


        args = parser.parse_args()
        blank_string_checking=[args["productName"]]

        msg=["productName"]


        message = catchEmptyString(blank_string_checking,msg)
        if message:
            return {"message":message}
        else:
            return args








        return args
