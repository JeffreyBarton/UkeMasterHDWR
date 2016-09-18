from time import sleep
import json
import CHIP_IO.GPIO as GPIO
import pyrebase


A  = "0100100000000000" #4608
Am = "0000100000000000" #16384
A7 = "0100000000000000" #2048
B  = "0000001101001000" #4676
Bm = "0000011100001000" #5188
B7 = "0000101101000000" #16964
C  = "0000000000010000" #2
Cm = "0000000001110000" #546
C7 = "0001000000000000" #8
D  = "0000111000000000" #17472
Dm = "0010110000000000" #17536
D7 = "0000101000000000" #16448
E  = "0000000100001110" #4372
Em = "0000000100100100" #292
E7 = "0000010100000000" #1028
F  = "0010100000000000" #16512
Fm = "1010000000010000" #32898
F7 = "0010100001000000" #17024
G  = "0000010100100000" #1060
Gm = "0001010000100000" #1064
G7 = "0010010100000000" #1156


__chord = {'A':A,'Am':Am,'A7':A7,\
		'B':B,'Bm':Bm,'B7':B7,\
		'C':C,'Cm':Cm,'C7':C7,\
		'D':D,'Dm':Dm,'D7':D7,\
		'E':E,'Em':Em,'E7':E7,\
		'F':F,'Fm':Fm,'F7':F7,\
		'G':G,'Gm':Gm,'G7':G7}

for i in range(8):
	GPIO.setup("XIO-P%s"%i, GPIO.OUT)
	GPIO.setup("CSID%s"%i, GPIO.OUT)





#GPIO.setup("GPIO1", GPIO.OUT)
#GPIO.setup("GPIO2", GPIO.OUT)
#GPIO.setup("GPIO3", GPIO.OUT)
#GPIO.setup("GPIO4", GPIO.OUT)
#GPIO.setup("GPIO5", GPIO.OUT)
#GPIO.setup("GPIO6", GPIO.OUT)
#GPIO.setup("GPIO7", GPIO.OUT)


#GPIO.setup("CSID1", GPIO.OUT)
#GPIO.setup("CSID2", GPIO.OUT)
#GPIO.setup("CSID3", GPIO.OUT)
#GPIO.setup("CSID4", GPIO.OUT)
#GPIO.setup("CSID5", GPIO.OUT)
#GPIO.setup("CSID6", GPIO.OUT)
#GPIO.setup("CSID7", GPIO.OUT)


def showFrets(chord):
	#CSI 132 to 139
	#GPIO 408 to 415
	for i in range(8):
		t1 = int(chord[i])^1
		t2 = int(chord[i+8])^1
		GPIO.output("XIO-P%s"%i,t1)
		GPIO.output("CSID%s"%i,t2)

def boot():
	
	for i in range(16):
		showFrets(format(2^i,"016b"))
		sleep(1)

def stream_handler(post):
	c = __chord[post["data"]]
	print(c)
	showFrets(c)

if __name__ == "__main__":
	print("starting...")

	config = {
		"apiKey":"AIzaSyAs8v94X2JeQLpm7lP2rqcN7EtKwND_8tg",
		"authDomain": "ukemaster-fe566.firebaseapp.com",
		"databaseURL":"https://ukemaster-fe566.firebaseio.com/",
		"storageBucket": "ukemaster-fe566.appspot.com"
		}
	firebase = pyrebase.initialize_app(config)
	db = firebase.database()
	my_stream = db.child("Chords").child("Notes").stream(stream_handler)




#10.21.238.89

