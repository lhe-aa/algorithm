colors = ['B', 'G' , 'C']

colors_sequence = None
min = None

for color_0 in colors:
	bin_0  = 0
	bin_0_movement = get_movement(bin_0, color_0)
	for color_1 in colors:
		if color_1 != color_0:
			bin_1 = 1
			bin_1_movement = get_movement(bin_1, color_1)
			for color_2 in colors:
				if color_2 not in [color_0, color_1]:
					bin_2 = 1
					bin_2_movement = get_movement(bin_2, color_2)
		total_movement = bin_0_movement + bin_1_movement + bin_2_movement
		if not min or total_movement < min:
			min = total_movement
			colors_sequence = [color_0, color_1, color_2]
print("{}{}{} {}".format(colors_sequence[0], colors_sequence[1], colors_sequence[2], min))

get_movement(bin, color):
movement = 0
color_position = colors.index(color)
for bin_count in [0, 1, 2]:
	if bin_count != bin:
		movement += all_bottles[3 * bin_count + color_position]
return movement