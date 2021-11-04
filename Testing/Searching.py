def main():
    my_file = open("Super_Villains.txt")

    name_list = []

    for line in my_file:
        # line = line.strip()
        name_list.append(line)

    my_file.close()

    print(name_list)
    print("There were", len(name_list), "names in the file.")

    # linear search
    key = "Octavia the Siren"

    current_list_position = 0

    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1

    if current_list_position < len(name_list):
        print("The name is at position", current_list_position)

    else:
        print("The name was not in the list.")


main()
