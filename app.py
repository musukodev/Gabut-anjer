from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb://test:sparta@ac-o66gake-shard-00-00.iovsdoz.mongodb.net:27017,ac-o66gake-shard-00-01.iovsdoz.mongodb.net:27017,ac-o66gake-shard-00-02.iovsdoz.mongodb.net:27017/?ssl=true&replicaSet=atlas-jd8uu4-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # sample_receive = request.form['sample_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanmessages.find({}, {'_id': False}))
    return jsonify({'messages': message_list})

@app.route("/iklan")
def iklan():
    return render_template ("pisang.html")

@app.route("/iklanj")
def iklanj():
    return render_template ("judi.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)