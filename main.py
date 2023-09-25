from flask import render_template, Flask, redirect, url_for
import os

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.errorhandler(405)
def method_not_allowed(error):
  return redirect("/")

@app.errorhandler(404)
def page_not_found(error):
  return redirect("/")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)