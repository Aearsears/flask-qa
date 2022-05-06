import os
import asyncio
from flask import Flask
from flask import request
from flask import jsonify
from requests_html import HTMLSession
from threading import Thread
from pyppeteer import launch

app = Flask(__name__)

session = HTMLSession()

asyncio.set_event_loop(asyncio.new_event_loop())


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
        new_thread = Thread(target=between_callback, args=data)
        new_thread.start()
        new_thread.join()
        return "<p>OK</p>"
    else:
        return "<p>API is live.</p>"


def between_callback(args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(task(args))
    loop.close()


async def task(data):
    mlLink = "https://share.streamlit.io/aearsears/example-app-qa-generator/main?text=" + \
        data[0].replace(" ", "%20")
    browser = await launch(handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(mlLink)
    await browser.close()


@app.route('/qa', methods=['POST'])
def qa():
    if request.method == 'POST':
        if not request.data:
            return "<p>No body data...</p>"
        print(request.json)
        return request.json
    else:
        return "<p>API is live.</p>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
