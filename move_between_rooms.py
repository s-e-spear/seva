"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified Contaminated Ward: Zombie Apocalypse Survival game.
# The dictionary links a room to other rooms.
rooms = {"Elevator": {"west": "ER Room"},
        "ER Room": {"east": "Elevator", "west": "Triage"},
        "Triage": {"east": "ER Room"},
        }

current_room = "Elevator"

# Player will move room to room when told a certain direction.
# Player will continue to play the game until being told to exit. 

while True:
    print("You are in the", current_room)
    direction = input("Enter a direction or exit: ").lower()

    if direction == "exit":
        current_room = "exit"
        break
    elif direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
            
# Player will be told "Do not go that way" when the wrong direction is entered. 
        
    else:
        print("Do not go that way")


