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
    return time_difference


def kbfunc():
    # check if a key has been pressed
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

def get_duration(duration_options):
    # get the duration from the user
    print("Please select a duration")
    for option in duration_options:
        print(f"{duration_options.index(option)}. {option}")

    return duration_options[int(input("Please select a duration: "))]


def format_time(time, duration):
    # format the time
    if duration == "seconds":
        return time.seconds
    elif duration == "minutes":
        return time.seconds / 60
    elif duration == "hours":
        return time.seconds / 3600
    elif duration == "days":
        return time.seconds / 86400

    
 
def main():
    while True:
        duration_options = ["seconds", "minutes", "hours", "days"]
        duration = get_duration(duration_options)
        main_start_time = get_time()
        halt_button_pressed = False
        while not halt_button_pressed:
            print("waiting for button press")
            time.sleep(1)
            print()
            if kbfunc():
                end_time = get_time()
                time_count = count_time(main_start_time, end_time)
                formatted_time = format_time(time_count, duration)
                print(f"it has been {formatted_time} {duration} since the button was pressed")
                halt_button_pressed = True
            else:
                print("waiting for button press")
                    

        

if __name__ == "__main__":
    main()