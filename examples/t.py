import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(GPIO.BCM)
while True:
	if(GPIO.input(24)==0):
		print "1111"
        if(GPIO.input(24)==1):
		print "2222"
