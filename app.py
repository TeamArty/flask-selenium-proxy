import flask
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# > Define Flask App
app     = Flask(__name__)
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36')
print(options.binary_location)
driver  = webdriver.Chrome(options=options)
print(options.binary_location)


# > GET /
@app.get("/")
def get():
    if request.args.get("url", None) == None:
        return flask.Response("No URL Specified", mimetype="text/plain")
    
    global driver
    driver.get(request.args.get("url"))
    return flask.Response(driver.page_source, mimetype="text/plain")