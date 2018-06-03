from flask import Flask
from flask_restful import Api, Resource

def create_app(config_name='development'):
    app = Flask(__name__)
    initialize_extensions(app)
    return app

def initialize_extensions(app):
    from app.resource.rest3_product import plyPosition
    from app.resource.rest1_partner_category import partnerCategory
    from app.resource.rest4_product_catagory_ply_measurement import ProductCatPlyMeasurement
    api = Api(app)
    api.add_resource(plyPosition, "/plyPosition")
    api.add_resource(partnerCategory, "/partnercatagory")
    api.add_resource(ProductCatPlyMeasurement, "/productcatplymeasurement")
