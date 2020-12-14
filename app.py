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


# Home
@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


# Arrets par ligne
@app.route('/arrets_ligne')
def arrets():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT nom FROM arrets")
    arrets = cur.fetchall()
    if result > 0:
        return render_template('arrets_ligne.html', arrets)
    else:
        msg = 'No Lignes Found'
        return render_template('arrets_ligne.html', arrets)
    # Close connection
    cur.close()


# Lignes
@app.route('/lignes')
def lignes():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM lignes")

    lignes = cur.fetchall()

    if result > 0:
        return render_template('lignes.html', lignes=lignes)
    else:
        msg = 'No Lignes Found'
        return render_template('lignes.html', msg=msg)
    # Close connection
    cur.close()


# Ligne
@app.route('/ligne/<string:ID_LIGNE>/')
def ligne(ID_LIGNE):
    cur = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()

    cur.execute("SELECT * FROM arrets  natural join arrets_lignes WHERE ID_LIGNE = %s", [ID_LIGNE])
    cur2.execute("SELECT * FROM arrets  natural join arrets_lignes WHERE ID_LIGNE = %s", [ID_LIGNE])
    cur3.execute("SELECT * FROM bus  WHERE ID_LIGNE = %s", [ID_LIGNE])

    arret = cur.fetchall()
    ligne = cur2.fetchone()
    bus1 = cur3.fetchall()

    return render_template('ligne.html', ligne=ligne, arret=arret, bus1=bus1)


# Bus Form Class
class BusForm(Form):
    numero = StringField('numero', )
    immatriculation = StringField('immatriculation', )
    nombre_place = StringField('nombre_place', )
    id_ligne = StringField('id_ligne', )


# Add Bus
@app.route('/add_bus', methods=['GET', 'POST'])
def add_bus():
    form = BusForm(request.form)
    if request.method == 'POST' and form.validate():
        numero = form.numero.data
        immatriculation = form.immatriculation.data
        nombre_place = form.nombre_place.data
        id_ligne = form.id_ligne.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO bus(NUMERO,IMMATRICULATION,NOMBRE_PLACE,ID_LIGNE) VALUES(%s, %s, %s, %s)",
                    (numero, immatriculation, nombre_place, id_ligne))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Bus Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_bus.html', form=form)


print("update")


# Edit Bus
@app.route('/edit_bus/<string:ID_BUS>', methods=['GET', 'POST'])
def edit_bus(ID_BUS):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get bus by id
    cur.execute("SELECT * FROM bus WHERE ID_BUS = %s", [ID_BUS])

    bus = cur.fetchone()
    cur.close()
    # Get form
    form = BusForm(request.form)

    # Populate bus form fields
    form.numero.data = bus['NUMERO']
    form.immatriculation.data = bus['IMMATRICULATION']
    form.nombre_place.data = bus['NOMBRE_PLACE']
    form.id_ligne.data = bus['ID_LIGNE']

    if request.method == 'POST' and form.validate():
        numero = request.form['numero']
        immatriculation = request.form['immatriculation']
        nombre_place = request.form['nombre_place']
        id_ligne = request.form['id_ligne']

        # Create Cursor
        cur = mysql.connection.cursor()

        # app.logger.info(numero)
        # Execute
        cur.execute("UPDATE bus SET NUMERO=%s, IMMATRICULATION=%s, NOMBRE_PLACE=%s, ID_LIGNE=%s WHERE ID_BUS=%s",
                    (numero, immatriculation, nombre_place, id_ligne, ID_BUS))
        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Bus Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_bus.html', form=form)


# Delete Bus
@app.route('/delete_bus/<string:id>', methods=['POST'])
def delete_bus(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM bus WHERE ID_BUS = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    flash('Bus Deleted', 'success')

    return redirect(url_for('dashboard'))


# Dashboard
@app.route('/dashboard')
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    # result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM bus ")

    busall = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', bus=busall)
    else:
        msg = 'No Bus'
        return render_template('dashboard.html', msg=msg)
    # Close connection
    cur.close()


@app.route('/arrets')
def all_stops():
    cur = mysql.connection.cursor()
    result = cur.execute("select * FROM arrets")
    stopall = cur.fetchall()

    if result > 0:
        return render_template('arrets.html', stopall=stopall)
    else:
        msg = 'No Stops'
        return render_template('dashboard.html', msg)


@app.route('/adress/<string:ID_ARRET>')
def adresse(ID_ARRET):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT ADRESSE FROM ARRETS where ID_ARRET = %s", [ID_ARRET] )
    adresse = cur.fetchall()

    if result > 0:
        return render_template('adress.html', adresse=adresse)
    else:
        msg = 'No adress'
        return render_template('dashboard.html', msg)


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
