def part1(game):
    return ord(game[-1]) - ord("W") + (3 if game in ("A X", "B Y", "C Z") else 6 if game in ("A Y", "B Z", "C X") else 0)

def part2(game):
    return 3 * (ord(game[-1]) - ord("X")) + (1 if game in ("A Y", "B X", "C Z") else 2 if game in ("A Z", "B Y", "C X") else 3)

with open('data.txt', 'r') as input:
    rows = [row.strip() for row in input]
    print(sum(part1(row) for row in rows))
    print(sum(part2(row) for row in rows))
