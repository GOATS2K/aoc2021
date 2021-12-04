import re
from typing import Match


def submarine_travel():
    horizontal = 0
    depth = 0

    with open("day02/input.txt", "r") as infile:
        directions: list[Match] = [
            re.match(r"^(\w+) (\d)$", line) for line in infile.readlines()
        ]

    for direction in directions:
        travel_direction = direction.group(1)
        travel_amount = int(direction.group(2))

        match travel_direction:
            case "forward":
                horizontal += travel_amount
            case "down":
                depth += travel_amount
            case "up":
                depth -= travel_amount

    print(f"Day 2, part 1: {horizontal * depth}")


if __name__ == "__main__":
    submarine_travel()
