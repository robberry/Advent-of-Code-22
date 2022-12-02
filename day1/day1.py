with open('data.txt', 'r') as input:
    elves = [[int(y) for y in x.split("\n")] for x in input.read()[:-1].split("\n\n")]
    print("Top elf: {}".format(max(sum(x) for x in elves)))
    print("Sum of top three elves: {}".format(sum(sorted([sum(x) for x in elves])[-3:])))
