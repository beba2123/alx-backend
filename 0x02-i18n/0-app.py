#!/usr/bin/env python 3
"""Create a single route and an index.html templates that
     that outputs Welcome to holberton.
"""
from flask import Flask, request, render_template
from os import getenv

app = Flask(__name__, static_url_path='')


@app.route('/', method=[GET], )