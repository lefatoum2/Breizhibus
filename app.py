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

print("connexion réussie")


# Lignes
@app.route('/')
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


print("route 1")


# Ligne
@app.route('/ligne/<string:ID_LIGNE>/')
def ligne(ID_LIGNE):
    cur = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    # Get article
    result = cur.execute("SELECT * FROM arrets  natural join arrets_lignes WHERE ID_LIGNE = %s", [ID_LIGNE])
    result2 = cur2.execute("SELECT * FROM arrets  natural join arrets_lignes WHERE ID_LIGNE = %s", [ID_LIGNE])

    arret = cur.fetchall()
    ligne = cur2.fetchone()
    return render_template('ligne.html', ligne=ligne, arret=arret)


# Bus Form Class
class BusForm(Form):
    numero = StringField('numero', [validators.Length(min=1, max=200)])
    immatriculation = StringField('immatriculation', [validators.Length(min=1, max=200)])
    nombre_place = StringField('nombre_place', [validators.Length(min=1, max=200)])
    id_ligne = StringField('id_ligne', [validators.Length(min=1, max=200)])


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

        return redirect(url_for('lignes'))

    return render_template('add_bus.html', form=form)


# Edit Bus
@app.route('/edit_bus/<string:ID_BUS>', methods=['GET', 'POST'])
def edit_bus(ID_BUS):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM bus WHERE ID_BUS = %s", [ID_BUS])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = BusForm(request.form)

    # Populate article form fields
    numero = form.numero.data
    immatriculation = form.immatriculation.data
    nombre_place = form.nombre_place.data
    id_ligne = form.id_ligne.data

    if request.method == 'POST' and form.validate():
        numero = request.form['numero']
        immatriculation = request.form['immatriculation']
        nombre_place = request.form['nombre_place']
        id_ligne = request.form['id_ligne']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(ID_BUS)
        # Execute
        cur.execute("UPDATE bus SET NUMERO=%s, IMMATRICULATION=%s, NOMBRE_PLACE=%s, ID_LIGNE=%s WHERE ID_BUS=%s", (numero, immatriculation, nombre_place, id_ligne, ID_BUS))
        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Bus Updated', 'success')

        return redirect(url_for('bus'))

    return render_template('edit_bus.html', form=form)


# Delete Bus
@app.route('/delete_bus/<string:ID_BUS>', methods=['POST'])
def delete_bus(ID_BUS):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM bus WHERE id = %s", [ID_BUS])

    # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    flash('Bus Deleted', 'success')

    return redirect(url_for('bus'))


# Bus
@app.route('/bus')
def bus():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    # result = cur.execute("SELECT * FROM bus")
    # Show articles only from the user logged in
    result = cur.execute("SELECT * FROM bus WHERE author = %s")

    articles = cur.fetchall()

    if result > 0:
        return render_template('bus.html', articles=articles)
    else:
        msg = 'No Bus Found'
        return render_template('bus.html', msg=msg)
    # Close connection
    cur.close()


# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
