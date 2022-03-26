from flask import Flask, render_template, request, flash, redirect, send_from_directory
import pymongo
from pymongo import MongoClient 
# client = MongoClient ('localhost', 27017)
# db = client.
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/HW2"


#main page
@app.route('/')
def index():
    return render_template("main_page.html")

#routing to page of authorization (that should lead to secret)
@app.route('/authorization', methods=['GET' , 'POST'])
def authorization():
    if request.method == 'GET':
        return render_template('auth/authorization.html')

#routing to page of registration (that should lead to secret)
@app.route('/signup', methods=['GET' , 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')

##routing to page with user profile
@app.route('/secret', methods=['GET' , 'POST'])
def secret():
    if request.method == 'GET':
        return render_template('auth/secret.html')



#3..2..1.. start!
app.run(host="localhost", port=5000, debug=True)