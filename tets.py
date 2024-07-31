import itertools


for item in itertools.count(3, 1):
    if item > 10:
        break
    print(item)