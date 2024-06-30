from flask import Blueprint, render_template, redirect, url_for, request, flash
import requests

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('index.html')