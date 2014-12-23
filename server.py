from flask import Flask, url_for, request, send_file
app = Flask(__name__)

import os.path
import json
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

