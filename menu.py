import sys
import os
import sample_image_generator
from text_box import TextBox


def print_menu(title, options,exit_message):

    counter = 1
    print (30 * '-')
    print(title)
    print (30 * '-')
    for i in options:
        print("("+str(counter)+")" + "\t" + str(i))
        counter += 1
    print("(0)" + "\t" + exit_message)

def menu():

    options = ["Client",
               "Project",
               "Date",
               "Name lenght",
               "Easteregg"]

    print_menu("Main menu", options, "Exit program")


def choice():
    choice = input('Enter your choice : ')
    choice = int(choice)

    if choice == 1:
        sample_image_generator.image_generator(TextBox.client())

    elif choice == 2:
        sample_image_generator.image_generator(TextBox.project())

    elif choice == 3:
        sample_image_generator.image_generator(TextBox.date())

    elif choice == 4:
        sample_image_generator.image_generator(TextBox.len_name())

    elif choice == 5:
        sample_image_generator.image_generator(TextBox.easteregg(0))

    elif choice == 5555:
        sample_image_generator.image_generator(TextBox.easteregg(1))

    elif choice == 0:
        sys.exit()

    else:
        print ("Invalid number. Try again...")


def main():
    while True:
        menu()
        try:
            choice()
        except ValueError as err:
            print("Oh shit. Something went wrong. Try again")

if __name__ == '__main__':
    main()
