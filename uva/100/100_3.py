import sys


def update(cache, to_be_updated, base_count):
    updated_len = len(to_be_updated)
    for i in range(updated_len):
        cache[to_be_updated[i]] = updated_len + base_count - i


def cal_cycle_length(cache, n):
    to_be_updated = []
    while n not in cache:
        to_be_updated.append(n)
        if n % 2 == 0:
            n = int(n / 2)  # Change from n/=2 to this format, run time from 1.49 to 2.14
        else:
            n = 3 * n + 1

    update(cache, to_be_updated, cache[n])
    return cache[n] + len(to_be_updated)


def solution():
    cache = {1: 1}
    for line in sys.stdin:
        max = 1
        if not line.strip():
            break
        begin, end = map(int, line.split())
        big, small = end, begin
        if begin > end:
            big, small = begin, end
        for x in range(big)[small - 1:]:
            step = cal_cycle_length(cache, x + 1)
            if step > max:
                max = step
        print("{} {} {}".format(begin, end, max))

# if __name__ == '__main__':
solution()
