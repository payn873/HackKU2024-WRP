'''
Creates urls for website
'''
from flask import Flask, request

app = Flask(__name__)
#Reads html text files for menu and search
fMenu = ''
with open('Menu.txt', 'r') as f:
    fMenu = f.read()
fSearch = ''
with open('search.txt', 'r') as f:
    fSearch = f.read()
#Sets up menu web page
@app.route('/')
def menu():
    fileText = ''
    for line in fMenu:
        fileText += line
    return fileText
#Sets up search web page for destocking
@app.route('/search/')
def destock():
    return fSearch
#Sets up storage web page
@app.route('/storage/')
def storage():
    return "Storage"
#Sets up another search webpage for restocking
@app.route('/restock/')
def restock():
    return fSearch

