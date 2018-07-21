import pygame
from pygame import display
import sys
from datetime import datetime

###############################################################################
# TODO: Create GUI window to display the current time in binary format.       #
###############################################################################

def binary_time( time_24hr ):
    
    # Variables
    switch = False
    time = ""
    b_time = ""

    # Converting user input
    for i, c in enumerate(time_24hr):
        if time_24hr[i] == ':':
            switch = True
        elif switch:
            time += time_24hr[i]
        else:
            time += time_24hr[i]
    
    time = int(time)

    # Converting integer time to binary time
    i = 10
    switch = False
    while i >= 0 and time >= 0:
        if pow(2, i) <= time:
            b_time += "1"
            time = time - pow(2, i)
            switch = True
        elif switch:
            b_time += "0"
        i -= 1

    print(b_time)

    return;

def main():
    # Initialize Pygame
    pygame.init()
    size = 200, 100
    window = pygame.display.set_mode(size)
    display.set_caption("Binary Clock")

    # Load Font
    font = pygame.font.Font(None, 80)
    text = 'Test'
    #size = font.size(text)

    render_text = font.render(text, 0, (250, 250, 250), (5, 5, 5))
    window.blit(render_text, (0, 0))

    pygame.display.flip()
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    
    now = datetime.now()
    cur_time = str(now.hour) + ":" + str(now.minute)
    print(cur_time)
    
    binary_time(cur_time)

    return 0;

main()
