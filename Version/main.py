#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, redirect
import sqlite3

star = "************"

conn = sqlite3.connect('database.db')
print(star + "Opened database successfully" + star)

tb_create = 'CREATE TABLE cadeaux (firstname TEXT, lastname TEXT, email TEXT)'
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='cadeaux'"
if not conn.execute(tb_exists).fetchone():
    conn.execute(tb_create);
    print(star + "Table created successfully" + star)  # Pas beau, mais fonctionnel

conn.close()

app = Flask(__name__)
firstname_list = []
lastname_list = []
email_list = []


@app.route('/accueil')
def accueil():
    return render_template('accueil.html')


@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')


@app.route('/data', methods=['POST'])
def data():
    prenom = request.form['firstname']
    firstname_list.append(prenom)
    print(firstname_list)

    nom = request.form['lastname']
    lastname_list.append(nom)
    print(lastname_list)

    email = request.form['email']
    email_list.append(email)
    print(email_list)

    return redirect('/formulaire')


@app.route('/saved_list', methods=['POST', 'GET'])
def saved_list():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO cadeaux (firstname,lastname,email) VALUES (?,?,?)",
                    (firstname_list, lastname_list, email_list))
        conn.commit()
        msg = "Record successfully added"
        conn.close()
    return render_template('saved_list.html', firstname_list=firstname_list,
                           lastname_list=lastname_list, email_list=email_list)


@app.route('/list_db')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from cadeaux")

    rows = cur.fetchall();
    return render_template("list_db.html", rows=rows)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':

        try:
            frstnm = request.form['frstnm']
            lstnm = request.form['lstnm']
            ml = request.form['ml']
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO cadeaux (firstname,lastname,email) VALUES (?,?,?)",
                            (str(firstname[0]), str(lastname[0]), str(email[0])))

                conn.commit()
                msge = "Record successfully added"
        except:
            conn.rollback()
            msge = "error in insert operation"

        finally:
            return render_template("result.html", msg=msge)
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
