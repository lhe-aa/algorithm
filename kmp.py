
def get_next(source):
    p_len = len(source)
    next_array = [0] * p_len
    next_array[0]  = -1
    k = -1
    j = 0
    step = 0
    while j < p_len -1:
        step += 1
        print "step: {}, k = {}, j = {}, array = {}".format(step, k, j, next_array)
        if k == -1 or source[j] == source[k]:
            k += 1
            j += 1
            next_array[j] = k
        else:
            k = next_array[k]
    
    print next_array

if __name__ == '__main__':
    get_next('abcabaad')
