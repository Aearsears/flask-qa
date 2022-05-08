import os
import asyncio
import urllib.parse
from flask import Flask
from flask import request
from flask import jsonify
from threading import Thread
from pyppeteer import launch

app = Flask(__name__)

asyncio.set_event_loop(asyncio.new_event_loop())

EXEC_PATH = os.environ.get(
    "GOOGLE_CHROME_SHIM", None)


@app.route("/")
def hello_world():
    return "<p>Hello!</p>"


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if not request.data:
            return "<p>No body data...</p>"
        data = request.json
        print(data["text"])
        new_thread = Thread(target=between_callback, args=(data,))
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
    print(data)
    mlLink = "https://share.streamlit.io/aearsears/example-app-qa-generator/main?text=" + \
        urllib.parse.quote(data["text"])
    browser = await launch(handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False,
                           headless=True,
                           executablePath=EXEC_PATH,
                           autoClose=False,
                           args=['--no-sandbox']
                           )
    page = await browser.newPage()
    await page.goto(mlLink, waitUntil="networkidle0")
    await page.content()
    elementHandle = await page.waitForSelector('div#root>div>div>div>iframe')
    frame = await elementHandle.contentFrame()
    await page.waitFor(10000)
    # await frame.waitForSelector('#status-code')
    # wait until the desired box appears
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
