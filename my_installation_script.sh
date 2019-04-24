#!/bin/bash

python3 -m venv ~/.virtualenvs/djangodev

pip3 install -r djangodev/requirement.txt

source ~/.virtualenvs/djangodev/bin/activate

pip3 install Django

django-admin startproject NoelSecret
