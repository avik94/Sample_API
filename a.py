from flask import Flask,request,jsonify


app =  Flask(__name__)

result=[{"name":"charls","salary":124,"dep":"python"}]

@app.route("/", methods=["GET","POST"])
def getiingData():
    if request.method=="GET":
        data=result
        return{"name":"charls","salary":124,"dep":"python"}

    else:
        result=[request.get_json["name"],request.get_json["salary"],\
             request.get_json["dev"]]
        return (jsonify(msg="Data Saved Successfully"))


if __name__ == '__main__':
    app.run()
