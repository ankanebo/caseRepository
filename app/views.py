from app import app
from flask import render_template, flash, redirect
from app import app
import flask
import requests
import sqlite3
import json
# import bd

# stop_start_data_base = False

# @app.route('/start_bd',  methods=['POST'])
# def start_end():
#     global stop_start_data_base
#     stop_start_data_base = not stop_start_data_base
#     bd.data_base()
#     return '{"status":"sucses"}'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
        title = 'кейс')

@app.route('/button_input', methods=['POST'])
def buton_1():
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    data = flask.request.get_json()
    SH = data["sh"]
    distance = data["distance"]
    print(SH)
    print(distance)
    return '{"status":"sucses"}'

