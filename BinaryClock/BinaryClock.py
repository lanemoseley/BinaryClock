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
        elif time[0] == 1:
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
        elif time[1] % 1 == 0 and time[1] > 0:
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
        elif time[2] % 1 == 0 and time[2] > 0:
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
    
    BinaryClock = Tk()
    BinaryClock.title("Binary Clock")

    label = Label(BinaryClock, text=binary_time(hour, minute, second))
    label.pack()

    BinaryClock.mainloop()

    return 0;

main()
