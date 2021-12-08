# flake8: noqa E501
def get_positioned_bits(file_contents: list[str]) -> list[str]:
    list_of_bits = []
    for i in range(12):
        bits_of_numbers = [line[i] for line in file_contents]
        positioned_bits = "".join(bits_of_numbers)
        list_of_bits.append(positioned_bits)
    return list_of_bits


def find_rating(contents: list[str], bit_index: int, most_common: bool) -> list[str]:
    pos_bits = get_positioned_bits(contents)
    target_bit = None

    if len(contents) == 2:
        if contents[0][-1] != contents[1][-1]:
            if most_common:
                contents = [line for line in contents if line[-1] == "1"]
            else:
                contents = [line for line in contents if line[-1] == "0"]
            return contents

    ones = pos_bits[bit_index].count("1")
    zeroes = pos_bits[bit_index].count("0")

    if ones > zeroes:
        most_common_bit = "1"
        least_common_bit = "0"
    else:
        most_common_bit = "0"
        least_common_bit = "1"

    if most_common:
        target_bit = most_common_bit
    else:
        target_bit = least_common_bit

    if ones == zeroes:
        if most_common:
            target_bit = "1"
        else:
            target_bit = "0"

    index_of_target_bit = []
    for i, number in enumerate(pos_bits[bit_index]):
        if number == target_bit:
            index_of_target_bit.append(i)

    contents = [
        item for counter, item in enumerate(contents) if counter in index_of_target_bit
    ]
    return contents


def calculate_ratings(most_common: bool) -> int:
    with open("day03/input.txt", "r") as infile:
        file_contents = [line.strip("\n") for line in infile.readlines()]

    i = 0
    while len(file_contents) != 1:
        file_contents = find_rating(file_contents, i, most_common=most_common)
        i += 1

    return int(file_contents[0], 2)


if __name__ == "__main__":
    oxygen_generator_rating = calculate_ratings(most_common=True)
    print(f"oxygen_generator_rating: {oxygen_generator_rating}")

    scrubber_rating = calculate_ratings(most_common=False)
    print(f"scrubber_rating: {scrubber_rating}")

    print(f"Answer: {scrubber_rating * oxygen_generator_rating}")
