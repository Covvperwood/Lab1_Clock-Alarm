from tkinter import *
import time
from time import strftime, localtime, sleep
import os
 

root = Tk()
time1 = ''
cth = 0
ctm = 0
cthb = 0
ctmb = 0
bol = True
clock = Label(root,font=('times', 50, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=10)
alarm_t=' '
tm = ' '

def chh():
    global cth
    global cthb
    if bol == True:
        cth+=1
    else:
        cthb+=1
        
def chm():
    global ctm
    global ctmb
    global cth
    global cthb
    if bol == True:
        ctm+=1
    else:
        ctmb+=1
    if (ctm + int(time.strftime('%M'))) % 60 == 0:
        cth+=1
    if (ctmb + int(time.strftime('%M'))) % 60 == 0:
        cthb+=1    
 
def tick():
    if bol == True:
        global time1
        global cth
        global ctm
        global tm
        global h_list
        time2 = time.strftime('%H:%M')
        if time2 != time1 or cth != 0 or ctm != 0:
            time1 = time2
            x0 = int(time1[0:2])
            y0 = int(time1[3:5])
            x = (x0 + cth) % 24
            y = (y0 + ctm) % 60
            if y < 10:
                tm = str(x)+" : 0" + str(y)
            else:
                tm = str(x)+" : " + str(y)
            clock.config(text = tm)
    clock.after(200,tick)

def alarm():
    global alarm_t
    global cthb
    global cth
    global ctmb
    global ctm
    if bol == False:
        if (int(time1[3:5]) + ctmb + ctm) % 60 < 10 : 
            clock.config(text = str((int(time1[0:2]) + cthb + cth) % 24) + " : 0" + str((int(time1[3:5]) + ctmb + ctm) % 60) + " Alarm")
            alarm_t =str(int(time1[0:2]) + cthb + cth) + " : 0" + str(int(time1[3:5]) + ctmb + ctm)
        else:
            clock.config(text = str((int(time1[0:2]) + cthb + cth) % 24) + " : " + str((int(time1[3:5]) + ctmb + ctm) % 60) + " Alarm")
            alarm_t =str(int(time1[0:2]) + cthb + cth) + " : " + str(int(time1[3:5]) + ctmb + ctm)
    clock.after(200, alarm)           

def stopper():
    global bol
    if bol == True:
        bol = False
    else:
        bol = True
        
        
def getup():
    global alarm_t
    global tm
    if bol == True and alarm_t == tm:
        os.system('say "пора на работу"')
    clock.after(200, getup)            
    
    
h=Button(clock, command = chh, text = "H", height = 2, width = 5)        
m=Button(clock, command = chm, text="M", bg='green', height=2, width=5)
a=Button(clock, command = stopper, text="A", bg='green', height=2, width=5)    
h.place(x = 150, y = 300)
m.place(x = 225, y = 300)
a.place(x = 300, y = 300)

tick()
alarm()
getup()

root.geometry('500x400+300+200')
root.mainloop()


