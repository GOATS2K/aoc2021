def measure():
    with open("day01/input.txt", "r") as measurements:
        counter = 0
        last_value = None
        for line in measurements.readlines():
            if not last_value:
                last_value = int(line)
                continue

            if int(line) > last_value:
                counter += 1

            last_value = int(line)

    print(counter)


if __name__ == "__main__":
    measure()
