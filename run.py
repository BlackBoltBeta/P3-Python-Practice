import sys

from termcolor import colored, cprint

#Here are the color selections POSIBLE ERROR CHANGE THIS
print_yellow_bold = lambda x: cprint(x, "yellow", attrs=["bold"])
print_red_bold = lambda x: cprint(x, "red", attrs=["bold"])


def opening_function():
    """
    This is the welcome message and the instructions
    """
    print_yellow_bold(
        "Welcome to Madlads for Libs,\n" +
        "please select the theme of your madlibs"
    )
    main_choice()


def madlibs01():
    """
    Madlibs theme number 1
    """
    noun = input(colored("noun: ", "blue", attrs=["bold"]))
    verb = input(colored("verb: ", "blue", attrs=["bold"]))
    noun2 = input(colored("noun: ", "blue", attrs=["bold"]))
    noun3 = input(colored("noun: ", "blue", attrs=["bold"]))
    verb2 = input(colored("verb: ", "blue", attrs=["bold"]))
    noun4 = input(colored("noun: ", "blue", attrs=["bold"]))

    if noun.isalpha() == False:
        print_red_bold("Please provide a word")
        madlibs01()
    elif verb.isalpha() == False:
        print_red_bold("Please provide a word")
        madlibs01()
    elif noun2.isalpha() == False:
        print_red_bold("Please provide a word")
        madlibs01()
    elif noun3.isalpha() == False:
        print_red_bold("Please provide a word")
        madlibs01()
    elif verb2.isalpha() == False:
        print_red_bold("Please provide a word")
        madlibs01()
    elif noun4.isalpha() == False:
        print_red_bold("Please provide a word")
        madlibs01()
    else:
        madlibs = print_yellow_bold(
        f"hey! This is my {noun}. It is {verb} for {noun2}" +
        f" and we have fun with {noun3}. " +
        f"Make sure you {verb2} and eat {noun4}."
    )


def madlibs02():
    """
    Madlibs theme number 2
    """
    print("this is a filler for madlib number 2")

def madlibs03():
    """
    Madlibs theme number 3
    """
    print("this is a filler for madlib number 3")


def main_choice():
    selection = int(input(colored("select Madlibs theme: ", "blue", attrs=["reverse", "blink"])))

    """
    This function allows the user to select a theme
    """
    if selection == 1:
        madlibs01()
    elif selection == 2:
        madlibs02()
    elif selection == 3:
        madlibs03()
    else:
        print("Invalid selection, please try again")
        main_choice()

def main():
    opening_function()

main()
"""
def madlibs(selection, noun, verb, noun_two):
    madlibsArray=[f"I went to the zoo found {noun} and {verb} it while {noun_two} watched", f"I want to the hospital, I got {noun} in the {verb} {noun2}"]
    return madlibsArray[selection]

selection = input("selection: ")
noun = input("A noun: ")
verb = input("A verb: ")
noun_two = input("Another noun: ") 
madlibs(selection, verb , noun_two)
"""

"""
adjective11 = input("adjective one: ")
adjective12 = input("adjective two: ")
adjective13 = input("adjective three: ")
adjective14 = input("adjective four: ")
adjective15 = input("adjective five: ")

place11 = input("a place: ")
pieceofcloth11 = input("piece of clothing: ")

bodypart11 = input("a body part: ")
bodypart12 = input("another body part: ")
bodypart13 = input("a third body part: ")

noun11 = input("a noun: ")
noun12 = input("a second noun: ")

place12 = input("another place: ")

madlibs2 = f"Every year, you should go visit the doctor. It is a very {adjective11} visit. Usually you have to skip going to {place11} to go. Your doctor is usualy a/n {adjective12} man or wonam who is wearing a/an {adjective13} {pieceofcloth11}. They will look at your {bodypart11}, {bodypart12} and {bodypart13}. Sometimes, they can be very {adjective14}. Afterwards, they will give you a {noun11} and a {noun12}, and your mom or dad will take you to {place12} as a treat. All in all, the doctor's office isn't so {adjective15}."


print(madlibs)
"""
"""
madlibs2 = print(
    f"Every year, you should go visit the doctor. It is a very {adjective11}" +
    f" visit. Usually you have to skip going to {place11} to go. Your doctor " +
    f"is usualy a/n {adjective12} man or wonam who is wearing a/an " +
    f"{adjective13} {pieceofcloth11}. They will look at your {bodypart11}," +
    f" {bodypart12} and {bodypart13}. Sometimes, they can be very" +
    f" {adjective14}. Afterwards, they will give you a {noun11} and a " +
    f"{noun12}, and your mom or dad will take you to {place12} as a treat." +
    f" All in all, the doctor's office isn't so {adjective15}."
)
"""
