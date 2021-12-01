def sliding_window_measure():
    with open("day01/input.txt", "r") as measurements:
        lines = [int(x) for x in measurements.readlines()]

    groups = []
    for i, _ in enumerate(lines):
        end_pos = i + 3
        groups.append(lines[i:end_pos])

    last_group_value = None
    counter = 0
    for group in groups:
        if len(group) != 3:
            continue

        if not last_group_value:
            last_group_value = sum(group)
            continue

        if last_group_value < sum(group):
            counter += 1

        last_group_value = sum(group)
    print(counter)


if __name__ == "__main__":
    sliding_window_measure()
