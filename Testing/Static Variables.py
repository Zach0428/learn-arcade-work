# class Cat:
    # population = 0

    # def __init__(self, name):
        # self.name = name
        # Cat.population += 1

# def main():
    # cat1 = Cat("Pat")
    # cat2 = Cat("Pepper")
    # cat3 = Cat("Pouncy")

    # print("The cat population is:", Cat.population)


# class Dog():
    # def __init__(self):
        # self.age = 0
        # self.name = ""
        # self.weight = 0

    # def bark(self):
        # print("Woof says", self.name)

# def main():
    # my_dog = Dog()
    # my_dog.name = "Spot"
    # my_dog.weight = 20
    # my_dog.age = 3

    # my_other_dog = Dog()
    # my_dog.name = "Fluffy"
    # my_dog.weight = 20
    # my_dog.age = 3

    # my_other_dog.bark()
    # my_dog.bark()

# class Person():
    # def __init__(self):
        # self.name = ""
        # self.money = 0


# def main():
    # bob = Person()
    # bob.name = "Bob"
    # bob.money = 100

    # nancy = bob
    # nancy.name = "Nancy"

    # print(bob.name, "has", bob.money, "dollars.")
    # print(nancy.name, "has", nancy.money, "dollars.")


# def give_money1(person):
    # person.money += 100


# class Person():
    # def __init__(self):
        # self.name = ""
        # self.money = 0


# def main():
    # bob = Person()
    # bob.name = "Bob"
    # bob.money = 100

    # give_money1(bob)
    # print(bob.money)


# Wrong:
# class Dog():
    # def __init__(self):
        # self.age = 0
        # self.name = ""
        # self.weight = 0

    # def __init__(self):
        # print("New dog!")


# class Dog():

    # def __init__(self, new_name):
        # """ Constructor. """
        # self.name = new_name


# def main():
    # This creates the dog
    # my_dog = Dog("Spot")

    # Print the name to verify it was set
    # print(my_dog.name)

    # This line will give an error because
    # a name is not passed in.
    # her_dog = Dog()


# class Boat():
    # def __init__(self):
        # self.tonnage = 0
        # self.name = ""
        # self.is_docked = True

    # def dock(self):
        # if self.is_docked:
            # print("You are already docked.")
        # else:
            # self.is_docked = True
            # print("Docking")

    # def undock(self):
        # if not self.is_docked:
            # print("You aren't docked.")
        # else:
            # self.is_docked = False
            # print("Undocking")

# class Submarine(Boat):
    # def submerge(self):
        # print("Submerge!")


# class Person():
    # def __init__(self):
        # self.name = ""

# class Employee(Person):
    # def __init__(self):
        # Call the parent/super class constructor first
        # super().__init__()

        # Now set up our variables
        # self.job_title = ""

# class Customer(Person):
    # def __init__(self):
        # super().__init__()
        # self.email = ""

# def main():
    # john_smith = Person()
    # john_smith.name = "John Smith"

    # jane_employee = Employee()
    # jane_employee.name = "Jane Employee"
    # jane_employee.job_title = "Web Developer"

    # bob_customer = Customer()
    # bob_customer.name = "Bob Customer"
    # bob_customer.email = "send_me@spam.com"

# class Dog:
    # def __init__(self, age, name):
        # self.age = age
        # self.name = name

    # def bark(self):
        # print("Woof")


# def main():
    # my_dog = Dog(10, "Fluffy")
    # print(my_dog.name)




main()