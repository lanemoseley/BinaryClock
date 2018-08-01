from tkinter import *
from datetime import datetime

# Tkinter
BinaryClock = Tk()
BinaryClock.title("Binary Clock")

# Label
label = Label(BinaryClock, text="Current Time")
label.pack()

# Canvas
canvas = Canvas(BinaryClock, width=420, height=420)
canvas.pack()
    
# Clock Background, Image Copyright Algot Runeman 2013, CC0 (Creative Commons), http://runeman.org/articles/binary-clock/
clock = PhotoImage(file="BinaryClock.png")    
canvas.create_image(0, 0, anchor=NW, image=clock)

# Time Indicators
indicator = PhotoImage(file="dot.png")
    

def display_clock():
    
    #Get Current Time
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    time = [hour, minute, second]

    #Clear Canvas
    canvas.delete("ind")

    while time[0] > 0:
        # Hours > 20 (Scalar)
        if time[0] > 20:
            canvas.create_image(7, 161, anchor=NW, image=indicator, tags="ind")
            time[0] -= 20
        # Hours > 10 (Scalar)
        elif time[0] > 10:
            canvas.create_image(7, 209, anchor=NW, image=indicator, tags="ind")
            time[0] -= 10
        # Hours < 10
        elif time[0] % 8 == 0:
            canvas.create_image(55, 65, anchor=NW, image=indicator, tags="ind")
            time[0] -= 8
        elif time[0] % 4 == 0:
            canvas.create_image(55, 113, anchor=NW, image=indicator, tags="ind")
            time[0] -= 4
        elif time[0] % 2 == 0:
            canvas.create_image(55, 161, anchor=NW, image=indicator, tags="ind")
            time[0] -= 2
        else:
            canvas.create_image(55, 209, anchor=NW, image=indicator, tags="ind")
            time[0] -= 1
    
    while time[1] > 0:
        # Minutes
        if time[1] > 50:
            canvas.create_image(103, 209, anchor=NW, image=indicator, tags="ind")
            canvas.create_image(103, 113, anchor=NW, image=indicator, tags="ind")
            time[1] -= 50
        elif time[1] > 40:
            canvas.create_image(103, 113, anchor=NW, image=indicator, tags="ind")
            time[1] -= 40
        elif time[1] > 30:
            canvas.create_image(103, 209, anchor=NW, image=indicator, tags="ind")
            canvas.create_image(103, 161, anchor=NW, image=indicator, tags="ind")
            time[1] -= 30
        elif time[1] > 20:
            canvas.create_image(103, 161, anchor=NW, image=indicator, tags="ind")
            time[1] -= 20
        elif time[1] > 10:
            canvas.create_image(103, 209, anchor=NW, image=indicator, tags="ind")
            time[1] -= 10
        # Minutes < 10
        elif time[1] % 8 == 0:
            canvas.create_image(151, 65, anchor=NW, image=indicator, tags="ind")
            time[1] -= 8
        elif time[1] % 4 == 0:
            canvas.create_image(151, 113, anchor=NW, image=indicator, tags="ind")
            time[1] -= 4
        elif time[1] % 2 == 0:
            canvas.create_image(151, 161, anchor=NW, image=indicator, tags="ind")
            time[1] -= 2
        else:
            canvas.create_image(151, 209, anchor=NW, image=indicator, tags="ind")
            time[1] -= 1
   
    while time[2] > 0:
        # Seconds
        if time[2] > 50:
            canvas.create_image(199, 209, anchor=NW, image=indicator, tags="ind")
            canvas.create_image(199, 113, anchor=NW, image=indicator, tags="ind")
            time[2] -= 50
        elif time[2] > 40:
            canvas.create_image(199, 113, anchor=NW, image=indicator, tags="ind")
            time[2] -= 40
        elif time[2] > 30:
            canvas.create_image(199, 209, anchor=NW, image=indicator, tags="ind")
            canvas.create_image(199, 161, anchor=NW, image=indicator, tags="ind")
            time[2] -= 30
        elif time[2] > 20:
            canvas.create_image(199, 161, anchor=NW, image=indicator, tags="ind")
            time[2] -= 20
        elif time[2] > 10:
            canvas.create_image(199, 209, anchor=NW, image=indicator, tags="ind")
            time[2] -= 10
        # Seconds < 10
        elif time[2] % 8 == 0:
            canvas.create_image(247, 65, anchor=NW, image=indicator, tags="ind")
            time[2] -= 8
        elif time[2] % 4 == 0:
            canvas.create_image(247, 113, anchor=NW, image=indicator, tags="ind")
            time[2] -= 4
        elif time[2] % 2 == 0:
            canvas.create_image(247, 161, anchor=NW, image=indicator, tags="ind")
            time[2] -= 2
        else:
            canvas.create_image(247, 209, anchor=NW, image=indicator, tags="ind")
            time[2] -= 1

    
    BinaryClock.after(200, display_clock)
    

display_clock()
BinaryClock.mainloop()