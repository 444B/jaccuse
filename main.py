# we want to use the Raspberry pi sense hat
# from sense_hat import SenseHat
from datetime import datetime
import time
import tty
import sys
import termios

def get_time():
    # get the current time in UTC
    current_time = datetime.utcnow()
    return current_time


def count_time(start_time, end_time):
    # get the difference between the start and end times
    time_difference = end_time - start_time
    # return the difference
    return time_difference


def kbfunc():
    x = sys.stdin.fileno()
    old_settings = termios.tcgetattr(x)
    try:
        tty.setcbreak(x)
        answer = sys.stdin.read(1)
        print(answer)
    finally:
        termios.tcsetattr(x, termios.TCSADRAIN, old_settings)
    if answer:
        return True
    else:
        return False

def time_selector():
    x = sys.stdin.fileno()
    old_settings = termios.tcgetattr(x)
    try:
        tty.setcbreak(x)
        print(f"""
        Please select the time unit you want to use
        0. Seconds
        1. Minutes
        2. Hours
        3. Days""")
        answer = sys.stdin.read(1)
    finally:
        termios.tcsetattr(x, termios.TCSADRAIN, old_settings)
    match answer:
        case "0":
            return "seconds"
        case "1":
            return "minutes"
        case "2":
            return "hours"
        case "3":
            return "days"
        case _:
            print("Please select a valid option")
            return time_selector()

 
def main():
    while True:
        time_options = ["seconds", "minutes", "hours", "days"]
        # TODO add a selection menu to to decide if the time is in seconds, minutes, hours or days
        selected_time = time_selector()
        button_pressed = False
        # sets the start time of the current loop
        main_start_time = get_time()
        
        # wait for the button to be pressed
        while not button_pressed:
            if kbfunc():
                end_time = get_time()
                time = count_time(main_start_time, end_time)
                print(f"it has been {time} seconds since the button was pressed")
                button_pressed = True
            else:
                print("waiting for button press")
                
            
if __name__ == "__main__":

    # run the main function
    main()