########################################################
# Experimental primitive proto Gui for switching Pi Cam
# preview on via GUI button also attempt to
# capture stills pictures with GUI button
#
# Bampot1 18/11/2020
#
########################################################

from tkinter import *
from picamera import PiCamera
from time import sleep


a=Tk()
a.title("Test GUI for Camera Control")
camera = PiCamera()





def Preview():
    
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    
def TakeStill():
    global stillCount
    filename = "Test" +  str(stillCount) + ".jpg"
    camera.capture(filename)
    stillCount+=1
    


stillCount=1
frame = LabelFrame(a, padx=5, pady=5)
frame.pack(padx=200, pady=200)

Camera1 = Button(frame, text="Camera Preview")
Camera2 = Button(frame, text="Take Still")

Camera1.pack()
Camera2.pack()

Camera1.config(command=Preview)
Camera2.config(command=TakeStill)

