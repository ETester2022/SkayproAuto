def square(side):

    if side % 2 == 0 or (side % 2 == 1):
        print(int(side) * int(side))
    else:
        print(int(side * side + 1))

square(1.5)