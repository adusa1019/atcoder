def solve(string):
    s, x, y = string.split()
    s = s.split("T")
    x, y = int(x), int(y)
    move_all = [len(_s) for _s in s]
    pos_x = set([move_all[0]])
    pos_y = set([0])
    move_x = move_all[2::2] or None
    move_y = move_all[1::2] or None
    if move_x:
        for move in move_x:
            pos_x = {_x + move for _x in pos_x} | {_x - move for _x in pos_x}
    if move_y:
        for move in move_y:
            pos_y = {_y + move for _y in pos_y} | {_y - move for _y in pos_y}
    return "Yes" if x in pos_x and y in pos_y else "No"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
