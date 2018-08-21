# -*- coding: UTF-8 -*-

import os
import time

import shutil
import logging
import argparse
import subprocess
import svn.remote
from datetime import datetime

from flask_cors import CORS
from flask_api import status
from flask import Flask, render_template, request, flash, url_for,redirect
from flask_restful import reqparse, abort, Api, Resource
from module.config import Config
from database.models import Projects, Writers
from database.config import session, engine
from flask_mail import Mail, Message


# fix the encoding issue in python 2.7
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

LOG = logging.getLogger(__name__)
app = Flask(__name__, template_folder='template')

# avoid cors error
CORS(app)

# RestFul api
api = Api(app)

# email api
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/writers')
def writers():
    return render_template('writers.html')

@app.route('/addWriter', methods=['POST'])
def addWriters():
    print request.form
    writer = request.form['name']
    email = request.form['email']
    writer = Writers(writer, email, 0)
    try:
        session.add(writer)
        session.commit()
    except Exception as error:
        print error
        session.rollback()
    finally:
        session.close()
    return redirect(url_for('writers'))


@app.route('/dispatch', methods=['POST'])
def dispatch():
    """
        dispatch project to the writes
    """
    projectName = request.form['name']
    keyWords = request.form['keyWords']
    description = request.form['description']
    uploadPath = request.form['uploadPath']
    project = Projects(name=projectName,
        uploadPath = uploadPath,
        keyWords=keyWords,
        description=description,
        updatedTime=datetime.now())
    try:
        session.add(project)
        session.commit()
    except Exception as error:
        print error
        session.rollback()
    finally:
        session.close()
    return redirect(url_for('index'))

@app.route('/detail')
def detail():
    """
    Detail page of project
    """
    id = request.args.get("id")
    projectDetail = session.query(Projects).filter(Projects.id == id).all()
    return render_template("detail.html", projectDetail=projectDetail)


class getWrites(Resource):
    """
        get the writers' infomation
    """
    def get(self):
        writers = session.query(Writers.id, Writers.name, Writers.email).all()

        date = [{'id':i[0], 'name':i[1], 
                'email':i[2]} for i in writers]
        return date

api.add_resource(getWrites, '/getWrites/')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)