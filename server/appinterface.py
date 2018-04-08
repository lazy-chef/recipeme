from flask import Flask
from flask import request
from lazyclarifai import *

app = Flask('server') #i think this is correct
lc = lazyclarifai()

@app.route('/submit', methods = 'POST')

def submit():
	
	for ifile in files:
		ifile.save(filename)
		lc.start(filename)
	
@app.route('/search') #click the search button once all pics uploaded
def searchc():	
	lc.search()
