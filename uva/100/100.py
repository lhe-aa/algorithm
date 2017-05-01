
def cal_cycle_length(n):
    cycle = 1
    while n != 1:
        cycle += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n /= 2
    return cycle


if __name__ == '__main__':

    params = raw_input()
    while params:
        max = 1
        begin, end = map(int, params.split(' '))

        for x in range(end)[begin-1:]:
            step = cal_cycle_length(x + 1)
            if step > max:
                max = step
        print max
        params = raw_input()
        # print cal_cycle_length(22)
