import random



def main():
    print("Welcome to Cars!")
    print("You are Lightning McQueen running from Frank!")
    print("Frank wants to kill you for waking him up!")
    print("Don't let him catch you!")
    print("Good Luck!")

    miles_traveled = 0
    gas_light = 0
    engine_overheating = 0
    frank_traveled = -20
    gas_in_the_can = 3

    done = False
    while not done:
        print("A. Refuel with gas.")
        print("B. Ahead Full throttle.")
        print("C. Ahead half throttle.")
        print("D. Rest.")
        print("E. Status check.")
        print("F. Quit.")
        choice = input("What is your choice? ")
        if choice.lower() == "f":
            done = True
            print("See ya bum!")
        elif choice.lower() == "e":
            print("You have traveled", miles_traveled, "miles.")
            print("You have", gas_in_the_can, "left.")
            print("Frank is", (miles_traveled - frank_traveled), "miles behind you.")
        elif choice.lower() == "d":
            frank_traveled_now = random.randrange(7, 15)
            engine_overheating = 0
            frank_traveled += frank_traveled_now
            print("You had a good night rest.")
        elif choice.lower() == "a":
            print("You have refueled.")
        elif choice.lower() == "b":
            lightning_mcqueen_distance = random.randrange(10, 21)
            miles_traveled += lightning_mcqueen_distance
            print("You traveled", lightning_mcqueen_distance, "miles.")
            print("You were zooming.")
        elif choice.lower() == "c":
            lightning_mcqueen_distance = random.randrange(5, 13)
            miles_traveled += lightning_mcqueen_distance
            print("You traveled", lightning_mcqueen_distance, "miles.")
            print("You are cruising.")



main()