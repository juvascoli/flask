from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods= ['GET'])
def home():
    return{"message": "welcome to my api" }

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    #creating an user with received data
    return{"message": "user created"}
