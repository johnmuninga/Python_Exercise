
animal_locations = {}
animal_ids = []

print("Please enter the animal identity codes. (Press return when done.)")
while True:
    animal_id = input(f"Animal no. {len(animal_ids) + 1}:\n").strip()
    if animal_id == "":
        break
    animal_ids.append(animal_id)
    animal_locations[animal_id] = None

print("Commands: print, log animal_id x_ord y_ord, quit.")
while True:
    command = input(">").strip().split()
    if not command:
        continue

    if command[0] == "quit":
        break
    elif command[0] == "print":
        for animal_id in animal_ids:
            location = animal_locations[animal_id]
            if location:
                print(f"Animal {animal_id} last seen at ({location[0]}, {location[1]}).")
            else:
                print(f"Animal {animal_id} cannot be located.")
    elif command[0] == "log":
        if len(command) != 4:
            print("Invalid command format. Should be: log animal_id x_ord y_ord")
            continue
        animal_id, x_ord, y_ord = command[1], command[2], command[3]
        if animal_id not in animal_ids:
            print(f"Unknown animal ID: {animal_id}")
            continue
        try:
            x_ord = int(x_ord)
            y_ord = int(y_ord)
        except ValueError:
            print("The ordinates should be integers.")
            print("Commands: print, log animal_id x_ord y_ord, quit.")
            continue
        animal_locations[animal_id] = (x_ord, y_ord)
    else:
        print("Could not interpret command.")
        print("Commands: print, log animal_id x_ord y_ord, quit.")

