from tkinter import *
from datetime import datetime

def binary_time( hours, minutes, seconds ):
    
    # Variables
    time = [hours, minutes, seconds]   

    print("Input time: ", end = '')
    print(time)

    binary_clock = [["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]]

    while time[0] > 0:
        # Hours > 20 (Scalar)
        if time[0] > 20:
            binary_clock[2][0] = "[X]"
            time[0] -= 20
        # Hours > 10 (Scalar)
        elif time[0] > 10:
            binary_clock[3][0] = "[X]"
            time[0] -= 10
        # Hours < 10
        elif time[0] % 8 == 0:
            binary_clock[0][1] = "[X]"
            time[0] -= 8
        elif time[0] % 4 == 0:
            binary_clock[1][1] = "[X]"
            time[0] -= 4
        elif time[0] % 2 == 0:
            binary_clock[2][1] = "[X]"
            time[0] -= 2
        else:
            binary_clock[3][1] = "[X]"
            time[0] -= 1
    
    while time[1] > 0:
        # Minutes
        if time[1] > 50:
            binary_clock[3][2] = "[X]" # 1
            binary_clock[1][2] = "[X]" # 4
            time[1] -= 50
        elif time[1] > 40:
            binary_clock[1][2] = "[X]" # 4
            time[1] -= 40
        elif time[1] > 30:
            binary_clock[3][2] = "[X]" # 1
            binary_clock[2][2] = "[X]" # 2
            time[1] -= 30
        elif time[1] > 20:
            binary_clock[2][2] = "[X]" # 2
            time[1] -= 20
        elif time[1] > 10:
            binary_clock[3][2] = "[X]" # 1
            time[1] -= 10
        # Minutes < 10
        elif time[1] % 8 == 0:
            binary_clock[0][3] = "[X]"
            time[1] -= 8
        elif time[1] % 4 == 0:
            binary_clock[1][3] = "[X]"
            time[1] -= 4
        elif time[1] % 2 == 0:
            binary_clock[2][3] = "[X]"
            time[1] -= 2
        else:
            binary_clock[3][3] = "[X]"
            time[1] -= 1
   
    while time[2] > 0:
        # Seconds
        if time[2] > 50:
            binary_clock[3][4] = "[X]" # 1
            binary_clock[1][4] = "[X]" # 4
            time[2] -= 50
        elif time[2] > 40:
            binary_clock[1][4] = "[X]" # 4
            time[2] -= 40
        elif time[2] > 30:
            binary_clock[3][4] = "[X]" # 1
            binary_clock[2][4] = "[X]" # 2
            time[2] -= 30
        elif time[2] > 20:
            binary_clock[2][4] = "[X]" # 2
            time[2] -= 20
        elif time[2] > 10:
            binary_clock[3][4] = "[X]" # 1
            time[2] -= 10
        # Seconds < 10
        elif time[2] % 8 == 0:
            binary_clock[0][5] = "[X]"
            time[2] -= 8
        elif time[2] % 4 == 0:
            binary_clock[1][5] = "[X]"
            time[2] -= 4
        elif time[2] % 2 == 0:
            binary_clock[2][5] = "[X]"
            time[2] -= 2
        else:
            binary_clock[3][5] = "[X]"
            time[2] -= 1
    
    print("If correct, should be zero: ", end = '')
    print(time)

    # Display Clock
    print(binary_clock[0])
    print(binary_clock[1])
    print(binary_clock[2])
    print(binary_clock[3])

    return binary_clock;

def main():
   

    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    binary_time(hour, minute, second)
    

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
    hour_1 = PhotoImage(file="dot.png")
    hour_2 = PhotoImage(file="dot.png")
    hour_01 = PhotoImage(file="dot.png")
    hour_02 = PhotoImage(file="dot.png")
    hour_04 = PhotoImage(file="dot.png")
    hour_08 = PhotoImage(file="dot.png")

    min_1 = PhotoImage(file="dot.png")
    min_2 = PhotoImage(file="dot.png")
    min_4 = PhotoImage(file="dot.png")
    min_01 = PhotoImage(file="dot.png")
    min_02 = PhotoImage(file="dot.png")
    min_04 = PhotoImage(file="dot.png")
    min_08 = PhotoImage(file="dot.png")

    sec_1 = PhotoImage(file="dot.png")
    sec_2 = PhotoImage(file="dot.png")
    sec_4 = PhotoImage(file="dot.png")
    sec_01 = PhotoImage(file="dot.png")
    sec_02 = PhotoImage(file="dot.png")
    sec_04 = PhotoImage(file="dot.png")
    sec_08 = PhotoImage(file="dot.png")

    canvas.create_image(7, 209, anchor=NW, image=hour_1)
    canvas.create_image(7, 161, anchor=NW, image=hour_2)
    canvas.create_image(55, 209, anchor=NW, image=hour_01)
    canvas.create_image(55, 161, anchor=NW, image=hour_02)
    canvas.create_image(55, 113, anchor=NW, image=hour_04)
    canvas.create_image(55, 65, anchor=NW, image=hour_08)

    canvas.create_image(103, 209, anchor=NW, image=min_1)
    canvas.create_image(103, 161, anchor=NW, image=min_2)
    canvas.create_image(103, 113, anchor=NW, image=min_4)
    canvas.create_image(151, 209, anchor=NW, image=min_01)
    canvas.create_image(151, 161, anchor=NW, image=min_02)
    canvas.create_image(151, 113, anchor=NW, image=min_04)
    canvas.create_image(151, 65, anchor=NW, image=min_08)
    
    canvas.create_image(199, 209, anchor=NW, image=sec_1)
    canvas.create_image(199, 161, anchor=NW, image=sec_2)
    canvas.create_image(199, 113, anchor=NW, image=sec_4)
    canvas.create_image(247, 209, anchor=NW, image=sec_01)
    canvas.create_image(247, 161, anchor=NW, image=sec_02)
    canvas.create_image(247, 113, anchor=NW, image=sec_04)
    canvas.create_image(247, 65, anchor=NW, image=sec_08)
    
   
    BinaryClock.mainloop()

    return 0;

main()
