'''
This is a dictionary of pixel maps for the 8x8 LED matrix.

'''

# colors
O = (0, 0, 0) # off
B = (0, 255, 0) # black # WTF! If I change this to GREEN it suddenly works?
W = (255, 255, 255) # white

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
            "0": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, W, W
            ],
            "1": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, B, W, B,
                O, O, O, O, O, W, W, B,
                O, O, O, O, O, B, W, B,
                O, O, O, O, O, B, W, B,
                O, O, O, O, O, W, W, W
            ],
            "2": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, B,
                O, O, O, O, O, W, W, W
            ],
            "3": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, W, W, W
            ],
            "4": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, B, B, W
            ],
            "5": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, B,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, W, W, W
            ],
            "6": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, B,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, W, W
            ],
            "7": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, B, B, W
            ],
            "8": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, W, W
            ],
            "9": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, W, B, W,
                O, O, O, O, O, W, W, W,
                O, O, O, O, O, B, B, W,
                O, O, O, O, O, W, W, W
            ]
        },
        "second_decimal": {
            "0": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "1": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                B, W, B, O, O, O, O, O,
                W, W, B, O, O, O, O, O,
                B, W, B, O, O, O, O, O,
                B, W, B, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "2": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, B, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "3": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "4": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O
            ],
            "5": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, B, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "6": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, B, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "7": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O
            ],
            "8": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ],
            "9": [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                W, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O,
                B, B, W, O, O, O, O, O,
                W, W, W, O, O, O, O, O
            ]
        },
        "time": {
            "sec": [
                W, O, O, O, O, O, O, O,
                W, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ],
            "min": [
                W, O, W, O, O, O, O, O,
                W, O, W, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ],
            "hour": [
                W, O, W, O, W, O, O, O,
                W, O, W, O, W, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ],
            "day": [
                W, O, W, O, W, O, W, O,
                W, O, W, O, W, O, W, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
            ]
        }
    }
