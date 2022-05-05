import os
from flask import Flask
from flask import request
from flask import jsonify
from requests_html import HTMLSession

session = HTMLSession()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello!</p>"


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if not request.data:
            return "<p>No body data...</p>"
        data = request.json
        print(data)
        mlLink = "https://share.streamlit.io/aearsears/example-app-qa-generator/main?text=" + \
            data["text"].replace(" ", "%20")

        r = session.get('http://www.yourjspage.com')
        r.html.render()

        return "<p>OK</p>"
    else:
        return "<p>API is live.</p>"


@app.route('/qa', methods=['POST'])
def qa():
    if request.method == 'POST':
        if not request.data:
            return "<p>No body data...</p>"

        return request.json
    else:
        return "<p>API is live.</p>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
