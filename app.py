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
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
driver  = webdriver.Chrome(options=options)

# > GET /
@app.get("/")
def get():
    if request.args.get("url", None) == None:
        return flask.Response("No URL Specified", mimetype="text/plain")
    
    global driver
    driver.get(request.args.get("url"))
    return flask.Response(driver.page_source, mimetype="text/plain")

# > GET /cai
@app.get("/cai")
def post():
    if request.args.get("id", None) == None:
        return flask.Response("No id Specified", mimetype="text/plain")
    id = request.args.get("id", None)
    
    global driver
    driver.get("https://beta.character.ai/chat?char=" + id)
    javascript = f'''var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://beta.character.ai/chat/character/info/', false);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.setRequestHeader('Authorization', 'Token be4699378133b71855e683d63eba698f0f0d870c');
    xhr.send('{"external_id":"{id}"}');
    return xhr.response;
    '''
    result = driver.execute_script(javascript);
    
    return result
