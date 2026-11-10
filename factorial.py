#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 10th NOV 2026
# This program allows the user to enter a whole number. It then ,
#  uses a do..while loop to calculate the factorial of that number


def main():
    # get the user number
    user_number_str = input("Enter a positive number :")

    # initialise the counter and the factorial
    counter = 0
    factorial = 1

    # introduce the try statement
    try:
        user_number_int = int(user_number_str)
        if user_number_int >= 0:
            if not (user_number_int == 0) and not (user_number_int == 1):
                while True:
                    counter = counter + 1
                    factorial = factorial * counter
                    print(f"Tracking{counter} times through loop")
                    if user_number_int <= counter:
                        break

                print("")
                print(f"{user_number_int}! = {factorial}")
            else:
                print(f"{user_number_int}! = 1")
        else:
            print(f"{user_number_int} is not a positive integer")
    except:
        print(f"{user_number_str} is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
