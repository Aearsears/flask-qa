import os
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello!</p>"


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if not request.data:
            return "<p>No body data...</p>"
        return request.json
    else:
        return "<p>API is live.</p>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
