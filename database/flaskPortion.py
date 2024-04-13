'''
Creates urls for website
'''
from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)
fMenu = open('Menu.txt', 'r')
fSearch = open('search.txt', 'r')
@app.route('/')
def menu():
    fileText = ''
    for line in fMenu:
        fileText += line
    return fileText
@app.route('/destock/')
def store():
    fileText = ''
    for line in fSearch:
        fileText += line
    return fileText
@app.route('/storage/')
def storage():
    return "Storage"
@app.route('/restock/')
def restock():
    fileText = ''
    for line in fSearch:
        fileText += line
    return fileText


