def my_range(start, end=None):
    if end is None:
        start, end = 0, end
    yield start
    start += 1
    if start == end:
        raise StopIteration('end')


r = my_range(1, 3)
for i in r:
    print(i)