#!/usr/bin/env python
import RPi._GPIO as GPIO
#import request
import time

#used pin array (list)
pin_list = [23, 24, 25]
floor_list = [16, 17, 18]
florr_data_tmp = []
req_floor_dic = {}



#payload data for customize
data_payload_floor = ''
data_payload_zone = '6'
data_payload_side = '2'

#flag to determin if lift has been request
isLiftRequest = False

## Edit config for each slave machine
payload = { 
	'floor': data_payload_floor,
	'zone' : data_payload_zone,
	'side' : data_payload_side		
}
#request url
url = 'http://192.168.1.12/lserver/sv/getlift.php'


def GPIO_CallbackFunc(gpio_pin):
	#check if input is 0
	if GPIO.input(gpio_pin) == 0:
		#find requested floor from dictionry
		floor_data_tmp.append(req_floor_dic.get(gpio_pin))

	#r = requests.post(url, data=payload)
	time.sleep(0.01)

#init gpio and attach to callback
def GPIO_Initialize (gpio_pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(gpio_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.add_event_detect(gpio_pin, GPIO.FALLING, callback = GPIO_CallbackFunc, bouncetime = 500)
	print "Pin " + str(gpio_pin) + " set"
	return

def GPIO_Setup(gpio_pin):
	#init all pin in gpio_pin list
	for pin in gpio_pin:
		GPIO_Initialize(pin)

if __name__ == '__main__':
	#create dictionary
	req_floor_dic = dict(zip(pin_list, floor_list))
	
	#Pin initialize
	GPIO_Setup(pin_list)
	while True:
		pass	

def test_func():
	pass	 

def testestestest():
	pass