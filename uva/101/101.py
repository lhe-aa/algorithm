# Kind of template, fill algorithm in solution method

class Movement(object):

    def __init__(self, n):
        self.count = n
        self.position_map = self.init_position_map(n)
        self.location_map = self.init_location_map(n)

    def init_position_map(self, n):
        position_map = dict()
        for i in range(n):
            position_map[i] = i
        return position_map

    def init_location_map(self, n):
        location_map = dict()
        for i in range(n):
            location_map[i] = [i]
        return location_map

    def execute(self, command):
        if command == 'quit':
            self.print_location()
            return 1
        m_or_p, from_b, onto_or_over, to_b = self.parse(command)
        if self.is_valid_command(from_b, to_b):
            self._execute(m_or_p, from_b, onto_or_over, to_b)

    def parse(self, command):
        m_or_p, from_b, onto_or_over, to_b = command.split()
        return m_or_p, int(from_b), onto_or_over, int(to_b)

    def is_valid_command(self, from_b, to_b):
        return False if from_b == to_b or self.position_map[from_b] == self.position_map[to_b] else True

    def _execute(self, m_or_p, from_b, onto_or_over, to_b):
        if m_or_p == 'move':
            if onto_or_over == 'onto':
                self.move_onto(from_b, to_b)
            else:
                self.move_over(from_b, to_b)
        else:  # pipe
            if onto_or_over == 'onto':
                self.pipe_onto(from_b, to_b)
            else:
                self.pipe_over(from_b, to_b)

    def move_onto(self, from_b, to_b):
        from_pos = self.position_map[from_b]
        from_locations = self.location_map[from_pos]
        init_blocks = []
        for i in range(len(from_locations)):
            if from_locations[i] == from_b:
                init_blocks.extend(from_locations[i+1:])
                from_locations = from_locations[:i]
                self.location_map[from_pos] = from_locations

                break

        to_pos = self.position_map[to_b]
        to_locations = self.location_map[to_pos]
        for i in range(len(to_locations)):
            if to_locations[i] == to_b:
                init_blocks.extend(to_locations[i+1:])
                to_locations = to_locations[:i+1]
                self.location_map[to_pos] = to_locations
                self.location_map[to_pos].append(from_b)
                self.position_map[from_b] = to_pos

                break

        for i in init_blocks:
            self.position_map[i] = i
            self.location_map[i].append(i)


    def move_over(self, from_b, to_b):
        from_pos = self.position_map[from_b]
        from_locations = self.location_map[from_pos]
        init_blocks = []
        for i in range(len(from_locations)):
            if from_locations[i] == from_b:
                init_blocks.extend(from_locations[i+1:])
                from_locations = from_locations[:i]
                self.location_map[from_pos] = from_locations

                break

        to_pos = self.position_map[to_b]
        self.location_map[to_pos].append(from_b)
        self.position_map[from_b] = to_pos

        for i in init_blocks:
            self.position_map[i] = i
            self.location_map[i].append(i)

    def pipe_onto(self, from_b, to_b):
        from_pos = self.position_map[from_b]
        from_locations = self.location_map[from_pos]
        init_blocks = []
        removed_blocks = []
        for i in range(len(from_locations)):
            if from_locations[i] == from_b:
                removed_blocks.extend(from_locations[i:])
                from_locations = from_locations[:i]
                self.location_map[from_pos] = from_locations
                break

        to_pos = self.position_map[to_b]
        to_locations = self.location_map[to_pos]
        for i in range(len(to_locations)):
            if to_locations[i] == to_b:
                init_blocks.extend(to_locations[i+1:])
                to_locations = to_locations[:i+1]
                self.location_map[to_pos] = to_locations
                self.location_map[to_pos].extend(removed_blocks)
                for x in removed_blocks:
                    self.position_map[x] = to_pos
                break

        for i in init_blocks:
            self.position_map[i] = i
            self.location_map[i].append(i)

    def pipe_over(self, from_b, to_b):
        from_pos = self.position_map[from_b]
        from_locations = self.location_map[from_pos]
        removed_blocks = []
        for i in range(len(from_locations)):
            if from_locations[i] == from_b:
                removed_blocks.extend(from_locations[i:])
                from_locations = from_locations[:i]
                self.location_map[from_pos] = from_locations
                break

        to_pos = self.position_map[to_b]
        self.location_map[to_pos].extend(removed_blocks)
        for x in removed_blocks:
            self.position_map[x] = to_pos

    def print_location(self):
        for i in range(self.count):
            if self.location_map[i]:
                print('{}: {}'.format(i, ' '.join(map(str, self.location_map[i]))))
            else:
                print('{}:'.format(i))

import sys


def solution():
    number = input()
    mov = Movement(int(number))
    return_val = 0
    step = 1
    while return_val != 1:
        line = input()
        return_val = mov.execute(line)
        step += 1


# if __name__ == '__main__':
solution()