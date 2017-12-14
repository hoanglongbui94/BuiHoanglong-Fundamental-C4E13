def is_inside(point, rect):

    if point[0] in range(rect[0],rect[0]+rect[2]) and point[1] in range (rect[1],rect[1]+rect[3]):
        return True
    else:
        return False

is_inside([10,20],[30,40,30,30])

print(is_inside([10,20],[30,40,30,30]))
