import os
from flask import Flask
from flask import request
from flask import jsonify

from library.pipelines import pipeline

app = Flask(__name__)

pipe = pipeline("multitask-qa-qg")


def generate_QA(data):
    print(data["text"])
    return jsonify(pipe(data["text"]))


@app.route("/")
def hello_world():
    return "<p>Hello!</p>"


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if not request.data:
            return "<p>No body data...</p>"
        return generate_QA(request.json)
    else:
        return "<p>API is live.</p>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
