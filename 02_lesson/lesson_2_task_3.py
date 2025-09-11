def square(side):
    area = side * side
    if side % 1 == 0:
        return int(area)
    else:
        if area % 1 == 0:
            return int(area)
        else:
            return int(area) + 1
print(square(5.5))