from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Band, Album, Song

app = Flask(__name__)

engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/bands/')
def showBands():
	bands = session.query(Band).all()

	return "this page will show all bands"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)