from flask import Flask, render_template, jsonify, request
from flaskext.mysql import MySQL
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)