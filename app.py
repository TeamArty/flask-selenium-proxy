import flask
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc

# > Define Flask App
app     = Flask(__name__)
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36')
driver  = webdriver.Chrome(options=options)

options = uc.ChromeOptions()
options.binary_location = "/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
test = uc.Chrome(options=options)

# > GET /
@app.get("/")
def get():
    if request.args.get("url", None) == None:
        return flask.Response("No URL Specified", mimetype="text/plain")
    
    global driver
    driver.get(request.args.get("url"))
    return flask.Response(driver.page_source, mimetype="text/plain")
