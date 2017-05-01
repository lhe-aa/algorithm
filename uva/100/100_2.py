
import sys


def cal_cycle_length(n):
    cycle = 1
    while n != 1:
        cycle += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n /= 2
    return cycle

# if __name__ == '__main__':

for line in sys.stdin:
    max = 1
    if not line.strip():
        break
    begin, end = map(int, line.split())
    big, small = end, begin
    if begin > end:
        big, small = begin, end
    for x in range(big)[small - 1:]:
        step = cal_cycle_length(x + 1)
        # print step
        if step > max:
            max = step
    print("{} {} {}".format(begin, end, max))
