
import math


def decode(in_filename, out_filename):
    with open(in_filename, "r", encoding="utf-8") as file_in, \
            open(out_filename, "w", encoding="utf-8") as file_out:

        words = file_in.readlines()
        index = 0
        for line in words:
            split = line.split()
            index = index + 1
            empty = ""
            if index <= 3:
                file_out.write(line)

            else:
                for i in range(len(split)):
                    if int(split[i]) % 3 == 0:
                        split[i] = "0 "
                        empty += (split[i])
                    elif int(split[i]) % 3 == 1:
                        split[i] = "153 "
                        empty += (split[i])
                    else:
                        split[i] = "255 "
                        empty += (split[i])
                file_out.write(empty + "\n")



def main_part1():
    print(decode("files/part1.ppm", "out_filename.ppm"))

def negate(line):
    """
    This function takes the parameter line (guaranteed to be a string of integers between 0 and 255 inclusive)
    and negates each value in line by subtracting it from 255.

    :param line: a string with integers of values between 0 and 255 inclusive. The number of integers is a multiple of 3 (str)
    :return: returns a new string with the same number of integers, but each one is negated (str)
    """
    # turns line from a string into a list
    make_list = line.split()
    new_string = ""

    # this for loop goes through the integers in the list and subtracts them from 255
    for i in range(len(make_list)):
        new_int = 255 - int(make_list[i])
        new_string = new_string + str(new_int) + " "

    # returns the new string with negated values after removing the excess space in the string by using rstrip
    return new_string.rstrip(" ")


def grey_scale(line):
    """
    This function takes the parameter line (guaranteed to be a string of integers between 0 and 255 inclusive) and converts
    each set of r, g, b values within line to greyscale values. Within each set of r, g, b values, r, g, and b all take
    on the same greyscale value. If the greyscale value is greater than 255, then sets the greyscale value to 255.

    :param line: a string with integers of values between 0 and 255 inclusive. The number of integers is a multiple of 3 (str)
    :return: returns a new string with r, g, b values that have been converted to grey (str)
    """
    # turns line from a string into a list
    make_list = line.split()
    empty = ""

    # goes through every third integer in the list
    for i in range(0, len(make_list), 3):
        # sets the r value as the first integer out of every group of three
        r = int(make_list[i])
        # sets the g value as the second integer out of every group of three
        g = int(make_list[i+1])
        # sets the b value as the third integer out of every group of three
        b = int(make_list[i+2])

        # calculates the greyscale value
        grey = int(math.sqrt(r * r + g * g + b * b))
        # if the resulting greyscale value is greater than 255, sets it to 255
        if grey > 255:
            grey = 255

        # sets r, g, and b equal to the greyscale value
        r = str(grey)
        g = str(grey)
        b = str(grey)
        # creates a string from the new r, g, b values
        empty += r + " " + g + " " + b + " "

    # returns the new string with greyscale values after removing excess space in the string by using rstrip
    return empty.rstrip(" ")



def remove_color(line, color):
    """
    This function takes a parameter line (guaranteed to be a string of integers between 0 and 255 inclusive) and a color
    (must be red, green, or blue). The function sets the respective r, g, b values to 0 based on the color specified in
    the parameter.

    :param line: a string with integers of values between 0 and 255 inclusive. The number of integers is a multiple of 3 (str)
    :param color: red, green, or blue (str)
    :return: a string with the same number of integers as in line, but with the respective r, g, b values replaced with 0 (str)
    """
    # turns line from a string into a list
    make_line = line.split()
    string = ""

    # if color is red, sets the first integer in every group of three to 0
    if color == "red":
        for i in range(0, len(make_line), 3):
            make_line[i] = "0"
    # if color is green, sets the second integer in every group of three to 0
    elif color == "green":
        for i in range(1, len(make_line), 3):
            make_line[i] = "0"
    # if color is blue, sets the third integer in every group of three to 0
    elif color == "blue":
        for i in range(2, len(make_line), 3):
            make_line[i] = "0"

    # loops through make_line and adds every value to a string
    for i in range (0, len(make_line)):
        string += make_line[i] + " "

    # returns the new string with modified r, g, b after removing excess space in the string by using rstrip
    return string.rstrip(" ")



def main():
    # TODO: implement the following required items:
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. List the possible image manipulation functions and ask the user to
       choose one of them. If they don't enter a valid choice, ask them again.
    4. Perform the requested manipulation on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    """
    input_file = input ("input file name: \n")
    output_file = input ("output file name: \n")
    number = input ("modifications are: \n 1. negate \n 2. greyscale \n 3. remove red \n "
                                                       "4. remove green \n 5. remove blue \n"
                    "enter the number of the desired modification \n")

    # asks the user to put in a valid number if the original input is not an integer between 1 and 5 inclusive
    while number != "1" and number != "2" and number != "3" and number != "4" and number != "5":
        number = input("please enter a valid number\nenter the number of the desired modification\n")

    # opens a file of the user's specification and writes a new file with the output name
    with open(input_file, "r", encoding="utf-8") as file_in, \
            open(output_file, "w", encoding="utf-8") as file_out:

        words = file_in.readlines()
        index = 0
        # loops through and numbers each line in the file
        for line in words:
            index = index + 1

            # writes the first three lines (the header for the ppm image)
            if index <= 3:
                file_out.write(line)
            # changes the input file based on user specification and writes a new output file in ppm format accordingly
            else:
                if number == "1":
                    file_out.write(negate(line))
                elif number == "2":
                    file_out.write(grey_scale(line))
                elif number == "3":
                    file_out.write(remove_color(line, "red"))
                elif number == "4":
                    file_out.write(remove_color(line, "green"))
                elif number == "5":
                    file_out.write(remove_color(line, "blue"))

        print("done")

if __name__ == '__main__':
    main() 