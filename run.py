"""
noun = input("noun: ")
verb = input("verb: ")
noun2 = input("noun: ")
noun3 = input("noun: ")
verb2 = input("verb: ")
noun4 = input("noun: ")

madlibs = f"hey! Welcome to my {noun}. Here, we {verb} about {noun2} and we have fun with {noun3}. Make sure you {verb2} to my {noun4}."


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

selection = input("select Madlibs theme: ")


while True:
    if selection = 1:
        print(madlibs01)
    elif selection = 2:
        print(madlibs02)
    elif selection = 3:
        print(madlibs03)
    else:
        print(instructions)
"""

instructions = "Welcome to Madlads for Libs,\n" + "please select the theme of your madlibs"

print(instructions)

def madlibs(selection, noun, verb, noun_two):
    madlibsArray=[f"I went to the zoo found {noun} and {verb} it while {noun_two} watched", f"I want to the hospital, I got {noun} in the {verb} {noun2}"]
    return madlibsArray[selection]

selection = input("selection: ")
noun = input("A noun: ")
verb = input("A verb: ")
noun_two = input("Another noun: ") 
madlibs(selection, verb , noun_two)



    
