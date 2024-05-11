#!/usr/bin/env python3
"""Preliminary exercises for Part IIA Project GF2."""
import sys
from mynames import *


def open_file(path):
    """Open and return the file specified by path."""
    try:
        fo = open(path, 'r')
        return fo
    except IOError:
        print("Error - can't find file or read data")
        sys.exit()


def get_next_character(input_file):
    """Read and return the next character in input_file."""
    char = input_file.read(1)
    return char


def get_next_non_whitespace_character(input_file):
    """Seek and return the next non-whitespace character in input_file."""
    char = input_file.read(1)

    while char.isspace():                # keep skipping whitespace characters
        char = input_file.read(1)
    return char


def get_next_number(input_file):
    """Seek the next number in input_file.

    Return the number (or None) and the next non-numeric character.
    """
    char = input_file.read(1)

    if char.isdigit():
        number = char
        char = input_file.read(1)

        while char.isdigit():
            number = number + char
            char = input_file.read(1)

    else:
        number = None
    return [number, char]       # return a two-element list


def get_next_name(input_file):
    """Seek the next name string in input_file.

    Return the name string (or None) and the next non-alphanumeric character.
    """
    char = input_file.read(1)

    if char.isalpha():
        name, next_char = char, input_file.read(1)

        while next_char.isalnum():
            name = name + next_char
            next_char = input_file.read(1)

    else:
        name, next_char = None, char

    return [name, next_char]


def main():
    """Preliminary exercises for Part IIA Project GF2."""
    # Check command line arguments
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("Error! One command line argument is required.")
        sys.exit()

    else:
        print("\nNow opening file...")
        # Print the path provided and try to open the file for reading
        print('Path provided: ', arguments[0])
        ip_file = open_file(arguments[0])

        # Print out all the characters in the file, until the end of file
        print("\nNow reading file...")

        next_char = get_next_character(ip_file)
        while next_char != "":
            print(next_char, end='')
            next_char = get_next_character(ip_file)

        # Place the pointer back at the beginning of input file
        ip_file.seek(0, 0)

        # Print out all the characters in the file, without spaces
        print("\nNow skipping spaces...")
        next_char = get_next_non_whitespace_character(ip_file)
        while next_char != "":
            print(next_char, end='')
            next_char = get_next_non_whitespace_character(ip_file)

        ip_file.seek(0, 0)
        print('\n')

        print("\nNow reading numbers...")
        next_number = get_next_number(ip_file)
        while next_number[1] != "":
            if next_number[0] is not None:
                print(next_number[0], end=' ')
            next_number = get_next_number(ip_file)

        ip_file.seek(0, 0)
        print('\n')

        # Print out all the names in the file
        print("\nNow reading names...")
        next_name = get_next_name(ip_file)
        while next_name[1] != "":
            if next_name[0] is not None:
                print(next_name[0], end=' ')
            next_name = get_next_name(ip_file)

        ip_file.seek(0, 0)
        print('\n')

        print("\nNow censoring bad names...")
        # Print out only the good names in the file
        name_table = MyNames()
        bad_name_ids = [name_table.lookup("Terrible"),
                        name_table.lookup("Horrid"),
                        name_table.lookup("Ghastly"),
                        name_table.lookup("Awful")]

        next_name = get_next_name(ip_file)
        while next_name[1] != "":
            if next_name[0] is not None:
                index = name_table.lookup(next_name[0])
                if index not in bad_name_ids:
                    print(next_name[0], end=' ')
            next_name = get_next_name(ip_file)

        print('\n')


if __name__ == "__main__":
    main()
