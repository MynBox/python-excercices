import math


def paint_calc(height, width, cover):
    nr_cans = math.ceil(((height * width)/cover))
    print(f"You'll need {nr_cans} cans of paint.")
    



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
COVERAGE = 5
paint_calc(height=test_h, width=test_w, cover=COVERAGE)

