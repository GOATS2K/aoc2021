def calculate_ratings() -> None:
    with open("day03/input.txt", "r") as infile:
        file_contents = [line for line in infile.readlines()]

    co2_scrubber_rating = ""
    oxygen_generator_rating = ""

    for i in range(12):
        bits_of_numbers = [line[i] for line in file_contents]
        bits_of_numbers = "".join(bits_of_numbers)
