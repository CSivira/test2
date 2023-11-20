def asc_list(l: [int]):
    if len(l) == 0:
        yield []

    yield []
    for i in range(len(l)):
        h = l[i]
        t = l[i + 1:]
        yield [h]
        for sub in asc_list(t):
            if len(sub) != 0 and sub[0] > h:
                yield [h] + sub


if __name__ == '__main__':
    test = [1, 4, 3, 2, 5]
    for a in asc_list(test):
        print(a)
