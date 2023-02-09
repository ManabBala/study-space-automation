offset = 8
myWidth = 1920
myHeight = 1080


def setWindowSize(window_obj, w_ratio, h_ratio):  # ratio is like 1/4 == one fourth of the width or height
    # print(f"new window width_ratio={w_ratio}, new height_ratio={h_ratio}")
    newW = int(myWidth * w_ratio + offset * 2)
    newH = int(myHeight * h_ratio + offset)
    window_obj.resizeTo(newW, newH)
    # print(f"new window width={newW}, new height={newH}")


def ceil(num):
    if num.is_integer():
        return int(num)
    else:
        return int(num)+1


def positionToCoordinate(c, p):  # return the coordinate of the corners of the box positioned at the specified position
    bottom = ceil(p / c)
    global right

    if p % c == 0:
        right = c
    else:
        right = p % c

    top = bottom - 1
    left = right - 1

    # print(f"top_left, bottom_right coordinate: {top, left},{bottom, right} for position: {p}")
    return top, left, bottom, right


def moveWindowTo(window_obj, column, row, startGrid, endGrid):
    if endGrid < startGrid:
        raise Exception("endGrid must be greater or equal to startGrid.")

    # calculating all the final corner position of the window
    top, left, _, _ = positionToCoordinate(column, startGrid)
    _, _, bottom, right = positionToCoordinate(column, endGrid)

    # setting the desired window size based on start and end grid position
    width_ratio = 1 / (column / (right - left))
    height_ratio = 1 / (row / (bottom - top))
    setWindowSize(window_obj, width_ratio, height_ratio)

    # calculating new top_left coordinate of the window
    newLeft = int(myWidth / column) * left - offset
    newTop = int(myHeight / row) * top
    # print(f"new window position(x={newLeft},y={newTop}")
    print("moved:", window_obj.moveTo(newLeft, newTop))


