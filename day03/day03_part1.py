def calculate_gamma_and_epsilon_rate() -> None:
    with open("day03/input.txt", "r") as infile:
        file_contents = [line for line in infile.readlines()]

    sorted_strings = []
    # Each binary string is 12 characters long
    for i in range(12):
        for j in file_contents:
            try:
                sorted_strings[i] += j[i]
            except IndexError:
                sorted_strings.append(j[i])

    gamma_rate = ""
    epsilon_rate = ""
    for binary_string in sorted_strings:
        if binary_string.count("0") > binary_string.count("1"):
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    print(gamma_rate)
    print(epsilon_rate)

    gamma_rate_decimal = int(gamma_rate, 2)
    epsilon_rate_decimal = int(epsilon_rate, 2)

    print(f"Total power consumption: {gamma_rate_decimal * epsilon_rate_decimal}")


if __name__ == "__main__":
    calculate_gamma_and_epsilon_rate()
