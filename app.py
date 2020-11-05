from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

from flask_mysqldb import MySQLdb, MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import mysql.connector as mysqlpyth


app = Flask(__name__)

# Configuration MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'breizhibus'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# initialisation MYSQL
mysql = MySQL(app)