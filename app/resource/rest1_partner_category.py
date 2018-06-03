from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from app.helper.catchBlankString import catchEmptyString

resource_field = {
        "associatetId":fields.Integer,
        "associateCatId":fields.Integer,
        "name":fields.String,
        "gstno":fields.String
}

resource = {"associatetId": 2, "associateCatId": 1,   \
       "name":"Tyl{or", "gstno":"22AAAAA000002Z2"}

class partnerCategory(Resource):
    @marshal_with(resource_field, envelope= "data")
    def get(self):
        return resource

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)


        parser.add_argument("associatetId", required= True, type= int)
        parser.add_argument("associateCatId", required= True, type= int)
        parser.add_argument("name", required= True, type= str)
        parser.add_argument("gstno", required= True, type= str)

        args = parser.parse_args()

        blank_string_checking = [args["name"],args["gstno"]]

        msg = ["Name","gstno"]

        def catchEmptyString(blank_string_checking, msg):
            for pos,value in enumerate(blank_string_checking):
                print(pos,value)
                if not value:
                    return {"message":msg[pos]+" Cannot Be Blank"}

        message = catchEmptyString(blank_string_checking,msg)

        if message:
            return {"message":message}
        else:
            return args
