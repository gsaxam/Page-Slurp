"""
author: saksham.ghimire
email: gsaxam@gmail.com
date: 05/08/2016
"""
# python build-in imports
from flask import Flask, render_template, request
import httplib
import json

# package level imports
from html_digger import slurp_page

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/inputUrl', methods=['POST'])
def process_input_url():
    page_url = request.get_json()
    result = slurp_page(page_url['url'])
    print result
    return json.dumps(result), httplib.OK


if __name__ == '__main__':
    app.run(debug=True)
