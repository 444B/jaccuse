from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
sense.scroll_speed = 0.05
sense.clear(0, 255, 255)  # Blue


"""

  Jaccuse!

  A way to keep track of how long it has been since you have been jaccused.

"""

def get_orientation():
    '''Get the orientation of the Pi, using an arrow'''
    sense.clear()
    flipped = True
    arrow = "^"
    while flipped is True:
        sense.show_letter(arrow)
        for event in sense.stick.get_events():

            # Check if the joystick was pressed
            if event.action == "pressed":

                # Check which direction
                if event.direction == "up": # Up arrow
                    sense.set_rotation(0)
                    sense.show_letter(arrow)
                elif event.direction == "down": # Down arrow
                    sense.set_rotation(180)
                    sense.show_letter(arrow)
                elif event.direction == "left":
                    sense.set_rotation(90)
                    sense.show_letter(arrow)
                elif event.direction == "right":
                    sense.set_rotation(270)
                    sense.show_letter(arrow)
                

                elif event.direction == "middle": # Enter key
                    flipped = False


    

def get_duration():
    ''' Gets the duration from the user, returning a string'''
    sense.clear()
    duration_list = ["s", "m", "h", "d"]
    sense.show_message(duration_list) # show options in the list
    pointer = 0 # this pointer will be used to keep track of the users cycling of the list
    choice = ""
    loop = True
    sense.show_message(duration_list[pointer]) # show the first item in the list
    while loop is True:
        for event in sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":

                # Check which direction
                if event.direction == "left": # Left arrow
                    pointer -= 1
                    sense.show_message(duration_list[pointer])
                elif event.direction == "right": # Right arrow
                    pointer += 1
                    if pointer == len(duration_list):
                        pointer = 0
                    sense.show_message(duration_list[pointer])
                elif event.direction == "middle": # Enter key
                    choice = duration_list[pointer]
                    sense.clear()
                    loop = False


    return choice

def update_display(counter, duration):
    ''' Updates the display with the counter and duration '''

    if counter < 10: # we can use sense.show_letter for single digits
        print("it has been "+ str(counter) + " " + duration + " since the button was pressed")
        sense.show_letter(str(counter))
    elif counter >=10: #otherwise we need to use sense.show_message
        #TODO sense.show_message scrolls the value so we need to freeze it
        print("it has been "+ str(counter) + " " + duration + " since the button was pressed")
        sense.show_message(str(counter))



def main():
    '''Main function, will get the duration and then start the timer.'''
    #TODO add a way to stop the timer by pressing the button
    get_orientation()
    duration = get_duration() # string
    counter = 0
    halt_button_pressed = False
    main_loop = True

    while main_loop is True:
        while halt_button_pressed is False:
            if duration == "s":
                sleep(1)
                counter += 1
                update_display(counter, duration)
            elif duration == "m":
                sleep(60)
                counter += 1
                update_display(counter, duration)
            elif duration == "h":
                sleep(3600)
                counter += 1
                update_display(counter, duration)
            elif duration == "d":
                sleep(86400)
                counter += 1
                update_display(counter, duration)
            else:
                print("error")
                break





if __name__ == "__main__":
    main()
