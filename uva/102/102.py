colors = ['B', 'G', 'C']


def cal(all_bottles):
    bin_0_movement = 0
    bin_1_movement = 0
    bin_2_movement = 0
    color_0 = None
    color_1 = None
    color_2 = None
    # colors_sequence = None
    min_movements = None
    for color_0 in colors:
        bin_0 = 0
        bin_0_movement = get_movement(all_bottles, bin_0, color_0)
        for color_1 in colors:
            if color_1 != color_0:
                bin_1 = 1
                bin_1_movement = get_movement(all_bottles, bin_1, color_1)
                for color_2 in colors:
                    if color_2 not in [color_0, color_1]:
                        bin_2 = 2
                        bin_2_movement = get_movement(all_bottles, bin_2, color_2)
                        # print color_0, color_1, color_2
                        # print bin_0_movement, bin_1_movement, bin_2_movement
                        total_movement = bin_0_movement + bin_1_movement + bin_2_movement
                        if min_movements == None or total_movement < min_movements or (total_movement == min_movements and colors_sequence > [color_0, color_1, color_2]):
                            min_movements = total_movement
                            colors_sequence = [color_0, color_1, color_2]
    print("{}{}{} {}".format(colors_sequence[0], colors_sequence[1], colors_sequence[2], min_movements))


def get_movement(all_bottles, bin, color):
    movement = 0
    color_position = colors.index(color)
    for bin_count in [0, 1, 2]:
        if bin_count != bin:
            movement += all_bottles[3 * bin_count + color_position]
    return movement


import sys


def solution():

    for line in sys.stdin:
        if not line.strip():
            break
        # all_bottles = map(int, line.split())
        all_bottles = [int(x) for x in line.split()]
        cal(all_bottles)

# if __name__ == '__main__':
solution()

# 1 2 3 4 5 6 7 8 9
# 5 10 5 20 10 5 10 20 10
# Sample Output
# BCG 30
# CBG 50