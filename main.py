"""

  Jaccuse!

  A way to keep track of how long it has been since you have been jaccused of something.
  Run this in https://trinket.io/sense-hat to emulate a pi sense-hat.
  sense-hat api: https://pythonhosted.org/sense-hat/api/


"""

from time import sleep
from sense_hat import SenseHat
from pixel_dict import O, B, W, pixel_dict, pixel_map
sense = SenseHat()


def get_orientation():
    '''
    Description:
        Set the orientation of the Pi, using an question mark.
        Use the Sense Hat buttons to pick the orientation
    Inputs:
        - None

    Outputs:
        - None
    
    '''
    sense.clear()
    flipped = True
    direction_dict = {"up": 0, "down": 180, "left": 90, "right": 270}
    arrow = "?"
    while flipped is True:
        sense.show_letter(arrow)
        for event in sense.stick.get_events():

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
    '''
    Description:
        Gets the duration from the user, returning a string
    Inputs:
        - None

    Outputs:
        - choice: string
    
    '''
    sense.clear() # clears LED screen
    duration_list = ["sec", "min", "hour", "day"] # list of time options
    pointer = 0 # this pointer will be used to keep track of the users cycling of the list
    choice = ""
    loop = True
    # sense.show_message("Duration?", scroll_speed=0.05)
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

# overwrite the values in question_mark with the values in all_x
def change(canvas, paint):
    '''
    Description:
        Changes the pixel map by using points as pain

    Inputs:
        - canvas: list
        - paint: list

    Outputs:
    - list

    '''
    # TODO this code is working (Somehow!) and not efficient at all
    # 128 comparisons for each painting, 3 paintings = 384 comparisons every iteration
    # this happens either every second or minute or hour or day, depending on choice
    # this is not good
    # also it was only fixed by some voodoo magic on line 8
    for i in range(len(canvas)):
        if paint[i] == W:
            canvas[i] = paint[i]
        elif paint[i] == B:
            canvas[i] = O
        elif paint[i] == O:
            pass
    return canvas


def update_display(counter, duration):
    '''
    Description:
        Updates the display with the counter and duration
        
    Inputs:
        - counter: Int
        - duration: Str

    Outputs:
        - None
    
    '''
    sense.clear()
    string_counter = str(counter)
    canvas = pixel_map


    if len(string_counter) == 1:
        left = "0"
        right = string_counter[0]
    elif len(string_counter) == 2:
        left = string_counter[0]
        right = string_counter[1]
    else:
        pass

    canvas1 = change(canvas, pixel_dict["first_decimal"][right])
    canvas2 = change(canvas1, pixel_dict["second_decimal"][left])
    canvas3 = change(canvas2, pixel_dict["time"][duration])
    sense.set_pixels(canvas3)


    # if counter < 10: # we can use sense.show_letter for single digits
    #     print("it has been "+ str(counter) + " " + duration + " since the button was pressed")
    #     sense.show_letter(str(counter))
    # elif counter >=10: #otherwise we need to use sense.show_message
    #     print("it has been "+ str(counter) + " " + duration + " since the button was pressed")
    #     sense.show_message(str(counter))



def main():
    '''
    Description:
        1. Will get the duration and then 
        2. start the timer
        
    Inputs:
        - None

    Outputs:
        - None
    
    '''
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
