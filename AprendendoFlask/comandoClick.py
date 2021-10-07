import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    print('Initialized the database.')
