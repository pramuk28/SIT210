import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

red = 19
green = 24
blue = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(green,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(blue,GPIO.OUT,initial=GPIO.LOW)

root= tk.Tk()
root.title("GUI - 3 LED Blink ")

def TurnOff():
    GPIO.output(red,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(blue,GPIO.LOW)
    
def TurnOn():
    TurnOff()
    GPIO.output(var.get(),GPIO.HIGH)

var= tk.IntVar()

led1 = tk.Radiobutton(root, text ="RED",bg="red", variable=var,value=5, command=TurnOn).pack()
led2 = tk.Radiobutton(root, text ="GREEN",bg="blue", variable=var,value =10, command=TurnOn).pack()
led3 = tk.Radiobutton(root, text ="BLUE",bg="green", variable=var,value =15, command=TurnOn).pack()

tk.Exitbutton = tk.Button(root, text="EXIT",bg="yellow", command=root.destroy).pack()

root.mainloop()

GPIO.cleanup()
