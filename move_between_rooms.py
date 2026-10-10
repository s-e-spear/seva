rooms = {"Elevator": {"west": "ER Room"},
        "ER Room": {"east": "Elevator", "west": "Triage"},
        "Triage": {"east": "ER Room"},
        }

current_room = "Elevator"

while True:
    print("You are in the", current_room)
    direction = input("Enter a direction or exit: ").lower()

    if direction == "exit":
        current_room = "exit"
        break
    elif direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("Do not go that way")
