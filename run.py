import sys

from termcolor import colored, cprint


def opening_function():

    """
    This is the welcome message and the instructions
    """
    print(colored(
        "Welcome to Madlads for Libs,\n" +
        "please select the theme of your madlibs",
        "yellow", attrs=["bold"]))
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

    if noun.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif verb.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif noun2.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif noun3.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif verb2.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    elif noun4.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs01()
    else:
        madlibs1 = print(colored(
            f"hey! This is my {noun}. It is {verb} for {noun2}" +
            f" and we have fun with {noun3}. " +
            f"Make sure you {verb2} and eat {noun4}.",
            "yellow", attrs=["bold"])
        )


def madlibs02():
    """
    Madlibs theme number 2
    """
    print("NUMBER 2")  # AAAAAAAAAAAAAAAAAAAA
    adjective11 = input(colored("An adjective: ", "blue", attrs=["bold"]))
    adjective12 = input(colored("An adjective: ", "blue", attrs=["bold"]))
    adjective13 = input(colored("Another adjective: ", "blue", attrs=["bold"]))
    adjective14 = input(colored("Adjective please: ", "blue", attrs=["bold"]))
    adjective15 = input(colored("Adjective again: ", "blue", attrs=["bold"]))
    place11 = input(colored("A place: ", "blue", attrs=["bold"]))
    pieceofcloth11 = input(colored("Some clothing: ", "blue", attrs=["bold"]))
    bodypart11 = input(colored("a body part: ", "blue", attrs=["bold"]))
    bodypart12 = input(colored("another body part: ", "blue", attrs=["bold"]))
    bodypart13 = input(colored("a third body part: ", "blue", attrs=["bold"]))
    noun11 = input(colored("a noun: ", "blue", attrs=["bold"]))
    noun12 = input(colored("a second noun: ", "blue", attrs=["bold"]))
    place12 = input(colored("another place: ", "blue", attrs=["bold"]))

    if adjective11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective12.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective13.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective14.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif adjective15.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif place11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif pieceofcloth11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif bodypart11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif bodypart12.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif bodypart13.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif noun11.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif noun12.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    elif place12.isalpha() is False:
        pprint(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs02()
    else:
        madlibs2 = print(colored(
            f"Every year, you visit the doctor. It is very {adjective11}. " +
            f"Usually you have to skip going to {place11} to go." +
            f"Your doctor is usualy a {adjective12} person" +
            f"who is wearing a/an {adjective13} {pieceofcloth11}." +
            " They will look at your {bodypart11}" +
            f", {bodypart12} and {bodypart13}." +
            f"They can be very {adjective14}. Afterwards," +
            f"they will give you a {noun11} and a " +
            f"{noun12}, and then you will go to {place12} as a treat." +
            f" All in all, the doctor's office isn't so {adjective15}.",
            "yellow", attrs=["bold"])
        )


def madlibs03():

    """
    Madlibs theme number 3
    """
    color31 = input(colored("A color: ", "blue", attrs=["bold"]))
    adjective31 = input(colored("An adjective: ", "blue", attrs=["bold"]))
    time31 = input(colored("A time of day: ", "blue", attrs=["bold"]))
    adjective32 = input(colored("Second adjective: ", "blue", attrs=["bold"]))
    place31 = input(colored("A place: ", "blue", attrs=["bold"]))
    food31 = input(colored("Food: ", "blue", attrs=["bold"]))
    food32 = input(colored("Some more food: ", "blue", attrs=["bold"]))
    verb31 = input(colored("A verb: ", "blue", attrs=["bold"]))
    noun31 = input(colored("A noun: ", "blue", attrs=["bold"]))

    if color31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif adjective31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif time31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif adjective32.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif place31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif food31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif food32.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif verb31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    elif noun31.isalpha() is False:
        print(colored(
            "Please make sure you input only words", "red", attrs=["bold"]))
        madlibs03()
    else:
        madlibs3 = print(colored(
            f"Bats are {color31}, {adjective31} animals which have wings. " +
            f"They fly around at {time31} which scares people. " +
            f"Bats are {adjective32}. My pet bat lives in {place31}. " +
            f"I like to feed him {food31} and" +
            f"{food32}. He likes to {verb31}. " +
            f"I am his favorite person, but he also likes {noun31}. ",
            "yellow", attrs=["bold"])
        )


def main_choice():
    selection = int(input(colored(
        "select Madlibs theme: ", "blue", attrs=["reverse", "blink"]
        )))

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
