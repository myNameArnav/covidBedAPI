from logging import critical
from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

db_name = "beds"
DB_URI = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)


class Bed(db.Document):
    _id = db.IntField()
    criticalLevel = db.StringField()
    hospitalName = db.StringField()
    pincode = db.IntField()
    timeSlot = db.StringField()


@app.route('/api/populate_beds', methods=['POST'])
def populate_bed():
    p1 = Bed(_id=1, criticalLevel="critical", hospitalName="Max",
             pincode=110099, timeSlot="06:00 - 09:00")
    p2 = Bed(_id=2, criticalLevel="not critical", hospitalName="Fortis",
             pincode=110101, timeSlot="15:00 - 18:00")
    p1.save()
    p2.save()
    return make_response("Populated", 201)


@app.route('/api/booked_beds', methods=['GET'])
def booked_beds():
    arr = []
    for beds in Bed.objects:
        arr.append(beds)
    return make_response(jsonify(arr), 200)


@app.route('/api/book_bed', methods=['POST'])
def book_bed():
    content = request.json
    bed = Bed(_id=content['_id'], criticalLevel=content['criticalLevel'],
              hospitalName=content['hospitalName'], pincode=content['pincode'], timeSlot=content['timeSlot'])
    bed.save()
    return make_response("Created", 201)


@app.route('/api/reschedule/<id>', methods=['GET', 'PUT'])
def reschedule(id):
    if request.method == 'GET':
        bedObj = Bed.objects(_id=id)
        if bedObj:
            return make_response(jsonify(bedObj), 200)
        else:
            return make_response("Enter a valid id numeber", 404)
    elif request.method == 'PUT':
        content = request.json
        bedObj = Bed.objects(_id=id)
        bedObj.update(timeSlot=content["timeSlot"])
        return make_response(jsonify(bedObj), 202)


@app.route('/api/delete/<id>', methods=['DELETE'])
def delete_booking(id):
    bedObj = Bed.objects(_id=id)
    bedObj.delete()
    return make_response("Deleted", 200)


if __name__ == '__main__':
    app.run(debug=True)
