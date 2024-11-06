def reverseInt(x):
    reversed_x = 0

    if x > 0:
        x = str(x)
        reversed_x = int(x[::-1])
    elif x < 0:
        x = str(x)
        reversed_x = -int(x[:0:-1])

    if reversed_x < (-2) ** 31 or reversed_x > (2) ** 31 - 1:
        return 0
    else:
        return reversed_x
