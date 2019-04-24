#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, redirect
import sqlite3
import numpy as np

star = "************"

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
    return render_template('saved_list.html', firstname_list=firstname_list,
                           lastname_list=lastname_list, email_list=email_list)

@app.route('/result', methods=['POST', 'GET'])
def result():
	output = []
	phrase = ("Pour ce Secret Santa, {} va offrir un cadeau à {}!")
	people= np.array(firstname_list)
	index = np.array(range(0,len(people)))
	np.random.shuffle(index)
	for i in range(0,len(people)):
		if i+1 > len(people)-1:
			elem1 = people[index[i]]
			elem2 = people[index[0]]
		else:
			elem1 = (people[index[i]])
			elem2 = (people[index[i+1]])
		output.append(phrase.format(elem1,elem2))
	return render_template('result.html', output = output)
	
if __name__ == '__main__':
    app.run(debug=True)
