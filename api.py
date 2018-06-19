from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/avik/Documents/sample-flask/employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)


class EmployeeData(db.Model):
    __tablename__ = 'employee_data'
    personId = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20))
    phoneNo = db.Column(db.Integer)
    department = db.Column(db.String(20))
    employeeSpots = db.relationship('EmployeefavSports',backref='EmployeeData')

class EmployeefavSports(db.Model):
    __tablename__ = 'employee_favsports'
    sportsId = db.Column(db.Integer,primary_key=True)
    sportsName= db.Column(db.String(20))
    empolyeeId =db.Column(db.Integer,db.ForeignKey('employee_data.personId'))




db.create_all()

@app.route("/sports", methods=['POST'])
def postingSport():
    result=request.get_json(["sportsName"]),request.get_json(["empolyeeId"])
    db.session.add(result)
    db.session.commit()
    return(jsonify(msg="Data saved successfully "))



@app.route("/",methods = ['GET','POST'])
def getingPostingData():
    if request.method=='GET':
        employees = EmployeeData.query.all()
        data = []
        for employee in employees:
            temp = {
                "personId": employee.personId,
                "name": employee.name,
                "phoneNo": employee.phoneNo,
                "department": employee.department
            }
            data.append(temp)
        result = jsonify(data)
        return result

    else:
        try:
            result= request.get_json()["name"],request.get_json()["phoneNo"],request.get_json()["department"]
            if not request.get_json()["name"] or not request.get_json()["phoneNo"] or not \
            request.get_json()["department"]:
                for pos,value in enumerate(result):
                    if not value:
                        if pos == 0:
                            return (jsonify(msg="Name is required."),400)
                        elif pos == 1:
                            return (jsonify(msg="Phoneno is required."),400)
                        elif pos == 2:
                            return (jsonify(msg="Department is required."),400)
            elif (isinstance(request.get_json()["phoneNo"],int)== False):
                return jsonify(msg="Phoneno must be integer")

            data= EmployeeData(name=request.get_json()["name"],\
                            phoneNo=request.get_json()["phoneNo"],\
                            department=request.get_json()["department"])
            db.session.add(data)
            db.session.commit()

            return(jsonify(msg="Data saved successfully"),200)

        except Exception as e:
            try:
                if "name" not in request.get_json() or "phoneNo" not in request.get_json() or \
                "department" not in request.get_json():
                    return (jsonify(msg="Please fill all required fields"),400)
            except Exception as e:
                return (jsonify(msg="Failed to decode JSON object: Expecting values"),500)


@app.route("/<string:value>", methods=["DELETE","PUT"])
def deletingPutting(value):
    if request.method=="DELETE":
        deleteData = EmployeeData.query.filter_by(personId=value).first()
        db.session.delete(deleteData)
        db.session.commit()

        return(jsonify(msg="Data deleted successfully"),200)




if __name__ == '__main__':
    app.run(port=8001 ,debug=True)
