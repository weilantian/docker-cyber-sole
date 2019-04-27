#! /usr/bin/env python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import thread
from bs4 import BeautifulSoup
from time import time,localtime,strftime
from twilio.rest import Client
from time import sleep
from flask import Flask,render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path
d = path.dirname(__file__)
app = Flask(__name__)
code = '<h1>Nothing here</h1>'
updated_time = time()

account_sid = 'AC48a5e19bc3216c8d989b6a49491fd2af'
auth_token = 'b78a6784b0efbe8352f5119cce866274'
client = Client(account_sid,auth_token)

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/now_code')
def now_code():
    global code,updated_time
    soup = BeautifulSoup(code)
    safe_code = soup.getText()
    timeArray = localtime(updated_time)
    styled_time = strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return render_template('take_a_look_at_code.html', code=safe_code,updated_time=styled_time)

@app.route('/now_img')
def now_img():
    return render_template('screen_shot_view.html')
def make_screenshot():
    global driver
    driver.get('https://cybersole.io')
    driver.maximize_window()
    sleep(1)
    js = "window.scrollTo(0,300)"
    driver.execute_script(js)
    pic_location = driver.get_screenshot_as_file(d+'\static\shot.png')


def main():
    print '[Bot]main process starteddddd'


    global code, updated_time
    not_first_shot = False
    while True:
        sleep(30)
        print '[Bot]Start trying.'
        updated_time = time()
        r = requests.get(url='https://cybersole.io')
        new_code = r.text
        if new_code != code:

            # Do something here
            print "[Bot]We got something here"
            print "---The new code is--"
            print new_code
            code = new_code
            make_screenshot()
            if not_first_shot:
                message = client.messages.create(body="\n[SKY'sBOT TEST MESSAGE]Mr.HUGO, it's time to PURCHASE.",
                                                 from_='+17867890385', to='+8618858298361')
                print message.sid
            else:
                print '[Bot]We just made first hand shake with the server.'
                not_first_shot = True



def startServer():
    thread.start_new_thread(main,())
    app.run(debug=False, port=8080)


if __name__ == '__main__':

    startServer()





