from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://mryhan:mryhan@cluster0.cq5ursx.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp')
db = client.dbmryhan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)