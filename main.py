import time
import tty
import sys
import termios

def get_duration(duration_options): # get the duration from the user
    
    print("Please select a duration")
    for option in duration_options:
        print(f"{duration_options.index(option)}. {option}")
    duration = duration_options[int(input("Please select a duration: "))]
    return duration #returns a string

def update_display(counter, duration):
    print(f"it has been {counter} {duration} since the button was pressed")

def kbfunc(): # check if a key has been pressed, by reading the stdin file descriptor
    x = sys.stdin.fileno()
    old_settings = termios.tcgetattr(x)
    try:
        tty.setcbreak(x)
        answer = sys.stdin.read(1)
    finally:
        termios.tcsetattr(x, termios.TCSADRAIN, old_settings)
    if answer:
        print("Key pressed")
        return True
    else:
        print("No key pressed")
        return False

def main():
    while True:
        # get the duration, set the counter and the halt button variables
        duration_list = ["seconds", "minutes", "hours", "days"]
        duration = get_duration(duration_list)
        counter = 0
        halt_button_pressed = False
         
        if duration == "seconds": # will add the other options later, just testing with seconds for now
                    print("Seconds selected")
                    while not halt_button_pressed:
                        time.sleep(1)
                        counter += 1
                        print(counter)
                        update_display(counter, duration)
                        # Code fucks up here on the next if cycle, it doesn't seems to wait for a key press, breaking the counter
                        # I tried to Continue but that didnt help
                        if not kbfunc():
                            continue
                        else:   
                            break                 
        
        else:
            print("Please select a valid duration")
            duration = get_duration(duration_list)


if __name__ == "__main__":
    main()