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
        print_red_bold("Please make sure you input only words")
        madlibs01()
    elif verb.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs01()
    elif noun2.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs01()
    elif noun3.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs01()
    elif verb2.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs01()
    elif noun4.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs01()
    else:
        madlibs1 = print_yellow_bold(
        f"hey! This is my {noun}. It is {verb} for {noun2}" +
        f" and we have fun with {noun3}. " +
        f"Make sure you {verb2} and eat {noun4}."
    )


def madlibs02():
    """
    Madlibs theme number 2
    """
    print("NUMBER 2")
    adjective11 = input(colored("An adjective: ", "blue", attrs=["bold"]))
    adjective12 = input(colored("An adjective: ", "blue", attrs=["bold"]))
    adjective13 = input(colored("Another adjective: ", "blue", attrs=["bold"]))
    adjective14 = input(colored("Adjective please: ", "blue", attrs=["bold"]))
    adjective15 = input(colored("Adjective again: ", "blue", attrs=["bold"]))
    place11 = input(colored("A place: ", "blue", attrs=["bold"]))
    pieceofcloth11 = input(colored("A piece of clothing: ", "blue", attrs=["bold"]))
    bodypart11 = input(colored("a body part: ", "blue", attrs=["bold"]))
    bodypart12 = input(colored("another body part: ", "blue", attrs=["bold"]))
    bodypart13 = input(colored("a third body part: ", "blue", attrs=["bold"]))
    noun11 = input(colored("a noun: ", "blue", attrs=["bold"]))
    noun12 = input(colored("a second noun: ", "blue", attrs=["bold"]))
    place12 = input(colored("another place: ", "blue", attrs=["bold"]))

    if adjective11.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif adjective12.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif adjective13.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif adjective14.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif adjective15.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif place11.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif pieceofcloth11.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif bodypart11.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif bodypart12.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif bodypart13.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif noun11.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif noun12.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    elif place12.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs02()
    else:
        madlibs2 = print_yellow_bold(
        f"Every year, you visit the doctor. It is very {adjective11}. " +
        f"Usually you have to skip going to {place11} to go. Your doctor " +
        f"is usualy a {adjective12} person who is wearing a/an " +
        f"{adjective13} {pieceofcloth11}. They will look at your {bodypart11}," +
        f" {bodypart12} and {bodypart13}. They can be very" +
        f" {adjective14}. Afterwards, they will give you a {noun11} and a " +
        f"{noun12}, and then you will go to {place12} as a treat." +
        f" All in all, the doctor's office isn't so {adjective15}."
        )

def madlibs03():
    """
    Madlibs theme number 3
    """
    color31 = input(colored("A color: ", "blue", attrs=["bold"]))
    adjective31 = input(colored("An adjective: ", "blue", attrs=["bold"]))
    time31 = input(colored("A time of day: ", "blue", attrs=["bold"]))
    adjective32 = input(colored("A second adjective: ", "blue", attrs=["bold"]))
    place31 = input(colored("A place: ", "blue", attrs=["bold"]))
    food31 = input(colored("Food: ", "blue", attrs=["bold"]))
    food32 = input(colored("Some more food: ", "blue", attrs=["bold"]))
    verb31 = input(colored("A verb: ", "blue", attrs=["bold"]))
    noun31 = input(colored("A noun: ", "blue", attrs=["bold"]))

    if color31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif adjective31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif time31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif adjective32.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif place31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif food31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif food32.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif verb31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    elif noun31.isalpha() == False:
        print_red_bold("Please make sure you input only words")
        madlibs03()
    else:
        madlibs3 = print_yellow_bold(
        f"Bats are {color31}, {adjective31} animals which have wings. " +
        f"They fly around at {time31} which scares people. " +
        f"Bats are {adjective32}. My pet bat lives in {place31}. " +
        f"I like to feed him {food31} and {food32}. He likes to {verb31}. " +
        f"I am his favorite person, but he also likes {noun31}. "
    )


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

madlibs03 = print(
    f"Bats are so cool! They are MANDING, MANDING animals which have wings. " +
    f"They like to fly around at MANDING which makes some people scared of them. " +
    f"But bats are MANDING, and they don't want to hurt people. " +
    f"I have a pet bat that lives in MANDING." +
    f"I like to feed him MANDING and MANDING. He likes to MANDING. " +
    f"I am his favorite person, but he also likes MANDING. " +
    f"I want to convince my parents to get me MANDING more bats."
)

"""
