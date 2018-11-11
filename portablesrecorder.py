import sys
import datetime
import aiy
import aiy.voicehat
from wavrec import *
import SCfunctions as sc



rec = Recorder(channels=2)
#recfilestring = 'reperecording'+ datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")+'.wav'
count = 0



def initfile():
    global recfile
    global recfilestring
    global state
    state = "idle"
    recfilestring = 'reperecording'+ datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")+'.wav'
    recfile = rec.open(recfilestring, 'wb')

def recnow():
    global recfile
    recfile.start_recording()

def stoprec():
    global recfile
    recfile.stop_recording()
    

def on_button_press():
    global state
    global recfile
    global recfilestring
    global count
    count = count + 1
    print("timesbuttonpressed = " + str(count))
    print("onpressstate = " + state)
    if (state == "idle"):
        print('starting recording')
        recnow()
        state = "recording"
        led.set_state(aiy.voicehat.LED.BLINK)
    elif (state == "recording"):
        print('stopping recording')
        stoprec()
        state = "uploading"
        led.set_state(aiy.voicehat.LED.BLINK_3)
        sc.uploadtrack(recfilestring)
        initfile()
        led.set_state(aiy.voicehat.LED.PULSE_QUICK)
    elif (state == "uploading"):
        print("still uploading")
        initfile()


initfile()

led = aiy.voicehat.get_led()

# You may set any LED animation:
led.set_state(aiy.voicehat.LED.PULSE_QUICK)
#led.set_state(aiy.voicehat.LED.BLINK)

#aiy.voicehat.get_status_ui().set_state('starting')
button = aiy.voicehat.get_button()
button.on_press(on_button_press)

try:
    while True:
        char = sys.stdin.read(1)
        print ("You pressed: "+char)
        if char == 'a':
            print("start the recording")
            recnow(recfile)
        if char == 'b':
            print('stopping recording')
            stoprec(recfile)
  
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print ("\n", "where done here, keyboard interrupt") # print value of counter  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print ("Other error or exception occurred!" )


finally:  
    #led.stop() # this ensures a clean exit  
    print("the end")