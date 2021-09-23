temperature = input("What is the temperature in Fahrenheit? ")
temperature = int(input(temperature))
print(f"You said the temperature was {temperature}.")
if temperature > 90:
    print("It is hot outside.")
elif temperature > 30:
    print("It is cold outside")
else:
    print("It is not hot outside.")

print("Done")