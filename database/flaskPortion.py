'''
Creates urls for website
'''
from flask import Flask, request

app = Flask(__name__)
fMenu = ''
with open('Menu.txt', 'r') as f:
    fMenu = f.read()
fSearch = ''
with open('search.txt', 'r') as f:
    fSearch = f.read()
@app.route('/')
def menu():
    fileText = ''
    for line in fMenu:
        fileText += line
    return fileText
@app.route('/search/')
def store():
    return fSearch
@app.route('/storage/')
def storage():
    return "Storage"
@app.route('/restock/')
def restock():
    return fSearch
@app.route(f'/search/?search={request.form[search]}')
def stock():
    return 'success'
