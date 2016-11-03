from flask import Flask
from flask import request
from flask import render_template

import requests
import json
import socket
APP_KEY = '' # Get from https://dev.telstra.com/user/me/apps
APP_SECRET = '' # Get from https://dev.telstra.com/user/me/apps


app = Flask(__name__)

@app.route('/')




def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

	message = request.form['text']
	number = request.form['text_number']
	print ("received data:", number, message )
	#processed_text = text.upper()
	#number = text[:10]
	#message = text[10:50]
	string_to_return = 'Details: ' + number + '  ' + message + ' ===>message sent OK'
	sms_send(number, message)
	return string_to_return
	#return 0
	
def sms_send(cell_number, sms_txt):

	tokenPayload = {'client_id' : APP_KEY,
                'client_secret': APP_SECRET,
                'grant_type' : 'client_credentials',
                'scope' : 'SMS'}

	request = "https://api.telstra.com/v1/oauth/token"
	response = json.loads(requests.get(request, params = tokenPayload).text)
	TOKEN = response['access_token']

	payload = {'to': cell_number,
           'body': sms_txt}

	r = requests.post('https://api.telstra.com/v1/sms/messages', 
                  headers = {'Content-Type' : 'application/json',
                             'Authorization' : 'Bearer ' + TOKEN},
                  data = json.dumps(payload))

	#print (r.text)
	#print (r.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
	