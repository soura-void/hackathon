# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
import sys
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import json
import requests


def reverseGeocode(latlng):
	result = {}
	mapurl = "https://www.google.com/maps/place/"
	url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={0}&key=AIzaSyB4MFYxYWyw27JlS2okhkJM-W4zI0uvHCI'
	apikey = 'XXX'
	i = 0
	request = url.format(latlng, apikey)
	data = json.loads(requests.get(request).text)
	sizeofList = 0
	try:
		result = data['error_message']
		return result
	except:	
		if len(data['results']) > 0:
			result = data['results'][1]['formatted_address']
			li = list(result.split(" "))
			print('sizeoflist: ', li)
			sizeofList = len(li)
			print('sizeoflist: ', sizeofList)
			mapurl = mapurl + li[i]
			i = i+1
			while i < sizeofList:
				mapurl = mapurl + '+' + li[i]
				i = i+1
			return mapurl
				
def sendemail(latlng):
	fromaddr = "kavachhack@gmail.com"
	toaddr = "bankita@qti.qualcomm.com, svishnoi@qti.qualcomm.com, mohapatr@qti.qualcomm.com, anurdas@qti.qualcomm.com"

# list of email_id to send the mail 
	li = ["bankita@qti.qualcomm.com", "svishnoi@qti.qualcomm.com", "mohapatr@qti.qualcomm.com", "anurdas@qti.qualcomm.com"]

# instance of MIMEMultipart 
	msg = MIMEMultipart() 

# storing the senders email address 
	msg['From'] = fromaddr 

# storing the receivers email address 
	msg['To'] = toaddr 

# storing the subject 
	msg['Subject'] = "SOS Signal"

# string to store the body of the mail 
	location = reverseGeocode(latlng)
	body = "Location: " + location
#N_image = sys.argv[2]

# attach the body with the msg instance 
	msg.attach(MIMEText(body, 'plain'))
	filename = "photos.jpg"
	attachment = open("download.jpg", "rb") 

# instance of MIMEBase and named as p 
	p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
	p.set_payload((attachment).read()) 

# encode into base64 
	encoders.encode_base64(p) 

	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
	msg.attach(p) 

# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
	s.starttls() 

# Authentication 
	s.login(fromaddr, "KavachHack@18") 

# Converts the Multipart msg into a string 
	text = msg.as_string() 

# sending the mail 
	s.sendmail(fromaddr, li, text) 

# terminating the session 
	s.quit() 

#print('formatted address:', sendemail(sys.argv[1]))
