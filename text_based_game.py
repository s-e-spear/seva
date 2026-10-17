# Name: Sabrina Morehouse
# IT-140 Project Two
# Contaminated Ward: Survival of the Zombie Apocalypse

def show_instructions():
  print("Contaminated Ward: Survivial of the Zombie Apocalypse")
  print("Gather all 6 items before encountering the Mega Zombie!")
  print("Movement commands: go north, go south, go east, go west")
  print("Include to inventory: obtain 'item name'")

def main():
  rooms = {
    "Elevator": {"west": "ER Room"},
    "ER Room": {"east: "Elevator", "west": "Triage", "item": "First Aid Kit"},
    "Triage": {"east": "ER Room", "north": "Trauma Bay", "item": "Flashlight"},
    "Trauma Bay": {"south": "Triage", "east": "Security Office", "item": "Bottled Water"},
    "Security Office": {"west": "Trauma Bay", "east": "Operating Room", "item": "Key Card"},
    "Operating Room": {"west": "Security Office", "east": "Hot Lab", "item": "Gun"},
    "Hot Lab": {"west": "Operating Room", "south": "Microbiology Lab", "item": "Protective Mask"},
    "Microbiology Lab": {"north": "Hot Lab", "west": "Research Lab", "item": "Cure Medicine"},
    "Research Lab": {"east": "Microbiology Lab", "west": "Elevator", "villain": "Mega Zombie"}
  }

  current_room = "Elevator" 
  inventory = []

  show_instructions()
  
    while True:
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
      print("You see a", rooms[current_room]["item"])

    command = input("Enter your move: ").lower().strip()

    if command.startswith("go "):
      direction = command[3:]
      if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
      else:
        print("Do not go there.")

    elif command.startswith("obtain "):'
    item = command[7:]
    if "item" in rooms[current_room] and item == rooms[current_room]["item"].lower():
      inventory.append(rooms[current_room]["item"])
      # Delete the gathered item from the room.
      del rooms[current_room]["item"]
      print("Item collected and added to bag!"]
    else:
      print("That item is not here in this room.")

    elif command == "exit":
      print("Come play again sometime!")
      break

    else:
      print("That is not a valid command. You need to try again.")


  if __name__ == "__main__":
    main()
    
      
    
  
  
  
    
  

