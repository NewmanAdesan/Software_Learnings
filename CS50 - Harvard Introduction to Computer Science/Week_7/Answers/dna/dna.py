import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    # storing data of each candidate in a list of dictionary
    candidates = []

    with open(sys.argv[1], "r") as file:
        # declare a csv dictionary reader object
        reader = csv.DictReader(file)

        for row in reader:
            candidates.append(row)

    # TODO: Read DNA sequence file into a variable
    dna = ""

    with open(sys.argv[2], "r") as file:
        # read data in file into a string variable
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # create dictionary to store consecutive count of each sequence
    sequence_count = {}

    # get each STR repeat documented in the database
    for sequence in candidates[0]:
        if sequence != "name":
            sequence_count[sequence] = longest_match(dna, sequence)

    # TODO: Check database for matching profiles
    # loop through each candidate
    for candidate in candidates:

        match = 0

        # loop through each sequence
        for sequence in sequence_count:
            if sequence_count[sequence] == int(candidate[sequence]):
                match += 1
            else:
                break

        # if all sequence count match
        if match == len(sequence_count):
            print(candidate["name"])
            return

    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
