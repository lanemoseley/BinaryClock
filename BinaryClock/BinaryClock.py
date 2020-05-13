"""
Program Name: Binary Clock
Author: Lane Moseley
Date: 08/01/2018
Description: The program retrieves the current time and displays it to the
             user in a GUI window in binary format. The time is refreshed
             every 200 milliseconds.
"""
from tkinter import *
from datetime import datetime

HOURS_10 = 7
HOURS_1 = 55
MINUTES_10 = 103
MINUTES_1 = 151
SECONDS_10 = 199
SECONDS_1 = 247
ROW_1 = 209
ROW_2 = 161
ROW_4 = 113
ROW_8 = 65

# Tkinter
BinaryClock = Tk()
BinaryClock.title("Binary Clock")

# Canvas
canvas = Canvas(BinaryClock, width=320, height=320)
canvas.pack()
    
# Background Image
# (Algot Runeman 2013, CC0, http://runeman.org/articles/binary-clock/)
clock = PhotoImage(file="BinaryClock.png")    
canvas.create_image(0, 0, anchor=NW, image=clock)

# Indicator Image
indicator = PhotoImage(file="dot.png")


def display_clock():
    """
    This function retrieves the current time. The time data is separated into
    hours, minutes, and seconds. The function then clears the canvas of any time
    indicators left over from a previous run. Next, the function determines the
    binary value of each time value and places a red dot on the canvas in the
    appropriate location.
    """
    # Clear canvas of previous time indicators
    canvas.delete("ind")

    # Get current time
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second

    while hour > 0:
        # Hours
        if hour > 20:
            canvas.create_image(HOURS_10, ROW_2, anchor=NW, image=indicator, tags="ind")
            hour -= 20
        elif hour > 10:
            canvas.create_image(HOURS_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            hour -= 10
        # Hours < 10
        elif hour % 8 == 0:
            canvas.create_image(HOURS_1, ROW_8, anchor=NW, image=indicator, tags="ind")
            hour -= 8
        elif hour % 4 == 0:
            canvas.create_image(HOURS_1, ROW_4, anchor=NW, image=indicator, tags="ind")
            hour -= 4
        elif hour % 2 == 0:
            canvas.create_image(HOURS_1, ROW_2, anchor=NW, image=indicator, tags="ind")
            hour -= 2
        else:
            canvas.create_image(HOURS_1, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            hour -= 1
    
    while minute > 0:
        # Minutes
        if minute > 50:
            canvas.create_image(MINUTES_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            canvas.create_image(MINUTES_10, ROW_4, anchor=NW, image=indicator, tags="ind")
            minute -= 50
        elif minute > 40:
            canvas.create_image(MINUTES_10, ROW_4, anchor=NW, image=indicator, tags="ind")
            minute -= 40
        elif minute > 30:
            canvas.create_image(MINUTES_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            canvas.create_image(MINUTES_10, ROW_2, anchor=NW, image=indicator, tags="ind")
            minute -= 30
        elif minute > 20:
            canvas.create_image(MINUTES_10, ROW_2, anchor=NW, image=indicator, tags="ind")
            minute -= 20
        elif minute > 10:
            canvas.create_image(MINUTES_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            minute -= 10
        # Minutes < 10
        elif minute % 8 == 0:
            canvas.create_image(MINUTES_1, ROW_8, anchor=NW, image=indicator, tags="ind")
            minute -= 8
        elif minute % 4 == 0:
            canvas.create_image(MINUTES_1, ROW_4, anchor=NW, image=indicator, tags="ind")
            minute -= 4
        elif minute % 2 == 0:
            canvas.create_image(MINUTES_1, ROW_2, anchor=NW, image=indicator, tags="ind")
            minute -= 2
        else:
            canvas.create_image(MINUTES_1, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            minute -= 1
   
    while second > 0:
        # Seconds
        if second > 50:
            canvas.create_image(SECONDS_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            canvas.create_image(SECONDS_10, ROW_4, anchor=NW, image=indicator, tags="ind")
            second -= 50
        elif second > 40:
            canvas.create_image(SECONDS_10, ROW_4, anchor=NW, image=indicator, tags="ind")
            second -= 40
        elif second > 30:
            canvas.create_image(SECONDS_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            canvas.create_image(SECONDS_10, ROW_2, anchor=NW, image=indicator, tags="ind")
            second -= 30
        elif second > 20:
            canvas.create_image(SECONDS_10, ROW_2, anchor=NW, image=indicator, tags="ind")
            second -= 20
        elif second > 10:
            canvas.create_image(SECONDS_10, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            second -= 10
        # Seconds < 10
        elif second % 8 == 0:
            canvas.create_image(SECONDS_1, ROW_8, anchor=NW, image=indicator, tags="ind")
            second -= 8
        elif second % 4 == 0:
            canvas.create_image(SECONDS_1, ROW_4, anchor=NW, image=indicator, tags="ind")
            second -= 4
        elif second % 2 == 0:
            canvas.create_image(SECONDS_1, ROW_2, anchor=NW, image=indicator, tags="ind")
            second -= 2
        else:
            canvas.create_image(SECONDS_1, ROW_1
        , anchor=NW, image=indicator, tags="ind")
            second -= 1

    # Refresh clock with current time
    BinaryClock.after(200, display_clock)
    

# Display Clock
display_clock()
BinaryClock.mainloop()