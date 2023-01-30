"""

  Jaccuse!

  A way to keep track of how long it has been since you have been jaccused of something.
  Run this in https://trinket.io/sense-hat to emulate a pi sense-hat.


"""

from time import sleep
from sense_hat import SenseHat
# from pixel_dict import all
sense = SenseHat()


'''
This is a dictionary of pixel maps for the 8x8 LED matrix.

'''

# colors
O = (0, 0, 0) # off
X = (255, 255, 255) # white

# List
pixel_map = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O]

# Dictionary

pixel_dict = {
        "first_decimal": {
            0: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, X, X
            ],
            1: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, X, O,
                O, O, O, O, O, X, X, O,
                O, O, O, O, O, O, X, O,
                O, O, O, O, O, O, X, O,
                O, O, O, O, O, X, X, X
            ],
            2: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, O,
                O, O, O, O, O, X, X, X
            ],
            3: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, X, X, X
            ],
            4: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, O, O, X
            ],
            5: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, X, X, X
            ],
            6: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, X, X
            ],
            7: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, O, O, X
            ],
            8: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, X, X
            ],
            9: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, X, O, X,
                O, O, O, O, O, X, X, X,
                O, O, O, O, O, O, O, X,
                O, O, O, O, O, X, X, X
            ]
        },
        "second_decimal": {
            0: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            1: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, X, O, O, O, O, O, O,
                X, X, O, O, O, O, O, O,
                O, X, O, O, O, O, O, O,
                O, X, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            2: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            3: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            4: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O
            ],
            5: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            6: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            7: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O
            ],
            8: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ],
            9: [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O,
                O, O, X, O, O, O, O, O,
                X, X, X, O, O, O, O, O
            ]
        },
        "time": {
            "sec": {
                "unit": [
                X, O, O, O, O, O, O, O,
                X, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ]
            },
            "min": {
                "unit": [
                X, O, X, O, O, O, O, O,
                X, O, X, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ]
            },
            "hour": {
                "unit": [
                X, O, X, O, X, O, O, O,
                X, O, X, O, X, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ]
            },
            "day": {
                "unit": [
                X, O, X, O, X, O, X, O,
                X, O, X, O, X, O, X, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ]
            }
        }
        }



def get_orientation():
    '''Set the orientation of the Pi, using an question mark.
    Use the Sense Hat buttons to pick the orientation'''
    sense.clear()
    flipped = True
    direction_dict = {"up": 0, "down": 180, "left": 90, "right": 270}
    arrow = "^"
    while flipped is True:
        sense.show_letter(arrow)
        for event in sense.stick.get_events():
            print("Event: ", event)
            print("Event type: ", type(event))

            # Check if the joystick was pressed
            if event.action == "pressed":

                # Check which direction
                if event.direction == "up": # Up button
                    sense.set_rotation(direction_dict[event.direction])
                    sense.show_letter(arrow)
                elif event.direction == "down": # Down button
                    sense.set_rotation(direction_dict[event.direction])
                    sense.show_letter(arrow)
                elif event.direction == "left": # Left button
                    sense.set_rotation(direction_dict[event.direction])
                    sense.show_letter(arrow)
                elif event.direction == "right": # Right button
                    sense.set_rotation(direction_dict[event.direction])
                    sense.show_letter(arrow)
                elif event.direction == "middle": # Enter key
                    flipped = False # exits the loop


def get_duration():
    ''' Gets the duration from the user, returning a string'''
    sense.clear() # clears LED screen
    duration_list = ["sec", "min", "hour", "day"] # list of time options
    pointer = 0 # this pointer will be used to keep track of the users cycling of the list
    choice = ""
    loop = True
    sense.show_message("Duration?", scroll_speed=0.05)
    sense.show_message(duration_list[pointer], scroll_speed=0.05) # show the first item in the list
    while loop is True:
        for event in sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":

                # Check which direction
                if event.direction == "left": # Left arrow
                    pointer -= 1
                    sense.show_message(duration_list[pointer], scroll_speed=0.05)
                elif event.direction == "right": # Right arrow
                    pointer += 1
                    if pointer == len(duration_list):
                        pointer = 0
                    sense.show_message(duration_list[pointer], scroll_speed=0.05)
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
        print("it has been "+ str(counter) + " " + duration + " since the button was pressed")
        sense.show_message(str(counter))



def main():
    '''Main function, will get the duration and then start the timer.'''
    main_loop = True
    halt_button_pressed = False
    get_orientation()
    duration = get_duration() # string
    while main_loop is True:
        counter = 0
        halt_button_pressed = False
        while halt_button_pressed is False:
            events = sense.stick.get_events()
            if events:
                for button in events:
                    if button.direction ==  "middle" and button.action == "pressed":
                        counter = 0
                        halt_button_pressed = True

            else:
                if duration == "sec":
                    update_display(counter, duration)
                    sleep(1)
                    counter += 1
                elif duration == "min":
                    update_display(counter, duration)
                    sleep(60)
                    counter += 1
                elif duration == "hour":
                    update_display(counter, duration)
                    sleep(3600)
                    counter += 1
                elif duration == "day":
                    update_display(counter, duration)
                    sleep(86400)
                    counter += 1
                else:
                    print("error")
                    break





if __name__ == "__main__":
    main()
