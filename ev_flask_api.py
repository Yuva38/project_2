import pymongo
import flask
from flask import request, jsonify, Flask
from flask_cors import CORS, cross_origin

#################################################
# Database Setup
#################################################
#connecting to Mongo db
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.ev_data
income_collection = db.Income
station_collection = db.Stations

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#app.config["DEBUG"] = True

CORS(app, support_credentials=True)
#################################################
# Flask Routes
#################################################

@app.route("/")
@cross_origin(supports_credentials=True)
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/Income<br/>"
        f"/api/Stations"
    )

@app.route('/api/Stations', methods=['GET'])
def home():
    d = list(station_collection.find({},{"_id": False}))
    print(d)
    return jsonify(d)
    
@app.route('/api/Income', methods=['GET'])
def home2():
    d = list(income_collection.find({},{"_id": False}))
    print(d)
    return jsonify(d)

if __name__ == "__main__":
    app.run(debug=True)
