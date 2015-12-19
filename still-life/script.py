''' The code has been written by Rishi Gaurav Bhatanagar (@rishigb) for a #stilllife project (with @justusbruns) , all code written and tested
with Pi B/B+, in association with Workbench Projects'''
import picamera
import requests
import time
from datetime import datetime
import math
import tweepy
import os
''' The following code will be used to send a picture '''
url_image = 'https://still-life.herokuapp.com/pagemulti'
camera = picamera.PiCamera()
#camera.resolution =(640,360)
camera.sharpness = 5
#camera.resolution = (1920, 1080)
#camera.resolution = (1087,728)
camera.resolution = (1280,720) #suits the screens best, 650Kb file.
camera.crop=(0.1,0.1,0.8,0.8)
camera.awb_mode ='auto'
camera.quality = 2
camera.brightness =53
camera.exposure_compensation = -25
####################################### Image Posting #######################################################
def fileName (cur_name,post_name):
        files ={post_name:open(cur_name,'rb')}
        r = requests.post(url_image,files=files)
        if (r.status_code) ==200:
               	print "Posted"
        else:
               	print r.status_code
		restart()


####################################Capturing Image ##########################################################
def captureImage(initialName,finalName,timeInterval):
        camera.capture(initialName+'.jpg')
	time.sleep(timeInterval)
        fileName(initialName+'.jpg',finalName) #This function is going to add the extension to finalName
'''The image being captured here will be stored in the same folder as the code '''
################################### Tweet ##################
def Tweet():
        CONSUMER_KEY = ''
        CONSUMER_SECRET = ''
        ACCESS_KEY = ''
        ACCESS_SECRET = ''
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.secure = True
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        # access the Twitter API using tweepy with OAuth
        api = tweepy.API(auth)
        #getting the parameter passed via the shell command from the Arduino Sketch
        status = "Live now from #Bangalore #stilllife"
        fn = os.path.abspath('Rishi.jpg')
        #UpdateStatus of twitter called with the image file
        api.update_with_media(fn, status=status)
        print "tweet sent"

def restart():
	command = "/usr/bin/sudo /sbin/reboot "
    	import subprocess
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print "rebooting"

before_tweet = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
before_reboot = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
while True:
	try:
		captureImage("Rishi","image_stream",60)
		after = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
		if (((after - before_tweet).seconds)/3600) ==6:
			before_tweet = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
        		print "1 min tweet",(((after - before_tweet).seconds))
			Tweet()
		if (((after - before_reboot).seconds)/3600) ==12:
			before_reboot = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
			restart()
	except Exception,e:
		restart()



