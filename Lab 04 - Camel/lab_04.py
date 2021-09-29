import random


def main():
    print("Welcome to Cars!")
    print("You are Lightning McQueen running from Frank!")
    print("Frank wants to kill you for waking him up!")
    print("Don't let him catch you!")
    print("Good Luck!")

    lightning_mcqueen_distance = 0
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
            print("You have traveled", lightning_mcqueen_distance, "miles.")
            print("You have", gas_in_the_can, "left.")
            print("Frank is", (lightning_mcqueen_distance - frank_traveled), "miles behind you.")
        elif choice.lower() == "d":
            frank_traveled_now = random.randrange(7, 15)
            engine_overheating = 0
            frank_traveled += frank_traveled_now
            print("You had a good night rest.")
        elif choice.lower() == "a":
            if gas_in_the_can > 0:
                gas_in_the_can -= 1
                gas_light = 0
                print("You have refueled.")
            else:
                print("You don't have any gas left")
        elif choice.lower() == "b":
            miles_traveled = random.randrange(10, 21)
            lightning_mcqueen_distance += miles_traveled
            gas_light += 1
            moving_tiredness = random.randrange(1, 4)
            engine_overheating += moving_tiredness
            frank_traveled_now = random.randrange(7, 15)
            frank_traveled += frank_traveled_now
            print("You traveled", miles_traveled, "miles.")
            print("You were zooming.")
            if random.randrange(20) == 0:
                gas_in_the_can = 3
                gas_light = 0
                engine_overheating = 0
                print("You have found a gas station!")
        elif choice.lower() == "c":
            miles_traveled = random.randrange(5, 13)
            lightning_mcqueen_distance += miles_traveled
            print("You traveled", miles_traveled, "miles.")
            print("You are cruising.")
            gas_light += 1
            engine_overheating += 1
            frank_traveled_now = random.randrange(7, 15)
            frank_traveled += frank_traveled_now
            if random.randrange(20) == 0:
                gas_in_the_can = 3
                gas_light = 0
                engine_overheating = 0
                print("You have found a gas station!")
        else:
            print("Please pick again.")

        if not done:
            if lightning_mcqueen_distance >= 200:
                print("You have escaped Frank!")
                done = True

        if not done:
            if gas_light > 4 and gas_light <= 6:
                print("You need to refuel.")
            elif gas_light > 6:
                print("You are out of gas.")
                done = True

        if not done:
            if engine_overheating > 5 and engine_overheating <= 8:
                print("Engine is getting hot.")
            elif engine_overheating > 8:
                print("Your engine overheated")
                caught = (lightning_mcqueen_distance - frank_traveled)
                frank_traveled += caught
        if not done:
            if frank_traveled >= lightning_mcqueen_distance:
                print("You have been caught by Frank!")
                print("You have lost!")
                done = True
            elif (lightning_mcqueen_distance - frank_traveled) < 15:
                print("Frank is getting close!")


main()
