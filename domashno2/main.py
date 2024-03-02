def calculate_boxes(slamki):
    largeBox = 0
    mediumBox = 0
    smallBox = 0

    while(slamki > 0):
        if slamki >= 50:
            largeBox += 1
            slamki -= 50
        elif slamki >= 20:
            mediumBox += 1
            slamki -= 20
        else:
            smallBox += 1
            slamki -= 5
    return [largeBox, mediumBox, smallBox]


boxes = calculate_boxes(115)

print(f"Large boxes: {boxes[0]}, Medium boxes: {boxes[1]}, Small boxes: {boxes[2]}")
