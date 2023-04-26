def dirReduc(alist):
    opposite_directions = {
        'NORTH': 'SOUTH',
        "SOUTH": "NORTH",
        "EAST": 'WEST',
        'WEST': 'EAST'
    }
    direction_stack = []

    for direction in alist:
        if direction_stack and direction_stack[-1] == opposite_directions[direction]:
            direction_stack.pop()
        else:
            direction_stack.append(direction)
        return direction_stack