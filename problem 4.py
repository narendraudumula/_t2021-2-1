elements = [1, 2, 3, 2, 1, 3, 2, 1, 1, 4, 5, 4, 4]
counts = {}
for element in elements:
    if element in counts:
        counts[element] += 1
    else:
        counts[element] = 1

for element, count in counts.items():
    print(element, ":", count)