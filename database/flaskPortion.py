'''
Creates urls for website
'''
from flask import Flask, url_for, request, render_template
from markupsafe import escape

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
@app.route('/destock/')
def store():
    return fSearch
@app.route('/storage/')
def storage():
    return "Storage"
@app.route('/restock/')
def restock():
    return fSearch


