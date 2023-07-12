import tkinter
from tkinter import *
import speedtest
import tkinter.messagebox

option = ''

def display_speed():
    global option
    spdc = speedtest.Speedtest()
    if option == 'Download Speed':
        speed = (spdc.download())
    elif option == 'Upload Speed':
        speed = (spdc.upload())
    elif option == 'Ping':
        severnames = []
        spdc.get_servers(severnames)
        speed = (spdc.results.ping)

    speedWithUnits = ''
    if(speed<1000):
        speedWithUnits = str(round(speed, 3))+"bps"
    elif(speed<1000000):
        speedWithUnits = str(round(speed/1000, 3))+"Kbps"
    elif(speed<1000000000):
        speedWithUnits = str(round(speed/1000000, 3))+"Mbps"
    else:
        speedWithUnits = str(round(speed/1000000000, 3))+"Gbps"

    tkinter.messagebox.showinfo("Internet Speed Checker", "Internet " +option+" Speed is:"+speedWithUnits)

def downspeed():
    global option
    option = 'Download Speed'
    display_speed()

def upspeed():
    global option
    option = 'Upload Speed'
    display_speed()

def ping():
    global option
    option = 'Ping'
    display_speed()

window = tkinter.Tk()
window.title("Internet Speed Checker")
window.geometry('700x300')
bg = PhotoImage(file="./spdc_background.png")

Label(window,image=bg).place(x=0,y=0)

Label(window, text = 'Internet Speed Checker', 
      fg = 'black', font = ('Georgia', 15)).place(x=235, y=10)
Label(window, text = 'Select any option', 
      fg = 'black', font = ('Georgia', 12)).place(x=280, y=40)
Button(window, text = "Check Download Speed", bg = '#F7F7F6', font = ('Trebuchet MS', 15), foreground = 'blue', width = 20, 
       command = downspeed).place(x=230, y=80)
Button(window, text = "Check Upload Speed", bg = '#F7F7F6', font = ('Trebuchet MS', 15), foreground = 'red', width = 20, 
       command = upspeed).place(x=230, y=150)
Button(window, text = "Check Ping", bg = '#F7F7F6', font = ('Trebuchet MS', 15), foreground = '#732F4D', width = 20, 
       command = ping).place(x=230, y=220)

window.mainloop()