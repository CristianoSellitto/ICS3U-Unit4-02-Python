#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds the factorial of a number


def main():
    # Finds the factorial of a number

    number = input("Enter a number to calculate the factorial: ")
    try:
        integer = int(number)
        if integer > 0:
            answer = 1
            counter = 1
            while counter < integer:
                answer = answer * counter
                counter = counter + 1
            answer = integer * answer
            print("\n{0}! = {1}".format(integer, answer))
        elif integer == 0:
            print("\n0! = 1")
        else:
            print("\nError: {} is a negative integer.".format(integer))
    except ValueError:
        print("\nError: {} is not an integer.".format(number))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
