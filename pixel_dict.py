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
