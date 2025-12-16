import json

#Items

item_key = {
    "name": "Key",
    "description": "A small, brass key for your room",
    "can_be_picked_up": True
}

item_newspaper = {
    "name": "Newspaper",
    "description": "An old newspaper, it tells of a man who caught a large fish",
    "can_be_picked_up": True
}

PLAYER_INVENTORY = []


#Areas

room_lobby = {
    "id": "lobby",
    "name": "The Hotel Lobby",
    "description": "A large hotel lobby, brightly lit with blank, white walls",
    "items": [
        item_key
        ],
    "exits": {
        "north": "hallway"
    }
}

room_hallway = {
    "id": "hallway",
    "name": "The Ground Floor Hallway",
    "description": "A long hallway, painted the same white as the lobby",
    "items": [
        item_newspaper]
        ,
    "exits": {
        "south": "lobby"
    }
}

WORLD = {
    "lobby": room_lobby,
    "hallway": room_hallway
}

CURRENT_ROOM_ID = "lobby"


#Functions

def display_room_info(room_id):
    #retrieve's current room's entire dictionary
    current_room = WORLD[room_id]

    print(f"\n--- {current_room['name'].upper()} --- \n"
          f"{current_room['description']}")
    
    #Prints the name of every item found in the current room, if there are any
    if len(WORLD[CURRENT_ROOM_ID]["items"]) >= 1:
        print("You see around you:")
        [print(WORLD[CURRENT_ROOM_ID]["items"][position]["name"]) for position in range(len(WORLD[CURRENT_ROOM_ID]["items"]))]    

def try_move(direction):
    global CURRENT_ROOM_ID

    #Retrieves current room's exits
    current_exits = WORLD[CURRENT_ROOM_ID]["exits"]

    if direction in current_exits:
        #Update to new location
        CURRENT_ROOM_ID = current_exits[direction]
        display_room_info(CURRENT_ROOM_ID)
    else:
        print("You cannot go that way!")

def parse_command(command_string):
    #Input: "Go North"
    words = command_string.strip().lower().split()
    #Result: ["go", "north"]

    verb = None
    noun = None

    if len(words) >= 1:
        verb = words[0]
    if len(words) >= 2:
        noun = words[1]
    
    return verb, noun

def handle_action(verb, noun):

    if verb == "look":
        if not noun:
            print("Look where?")
        elif noun == "around":
            display_room_info(CURRENT_ROOM_ID)
        elif noun in ("north", "east", "south", "west"):
            if noun in WORLD[CURRENT_ROOM_ID]["exits"]:
                display_room_info(WORLD[CURRENT_ROOM_ID]["exits"][noun])
            else:
                print("There is nothing to see that way!")
        elif noun in [PLAYER_INVENTORY[position]["name"].lower() for position in range(len(PLAYER_INVENTORY))]:
            print(PLAYER_INVENTORY[noun]["description"])

    elif verb == "inventory":
        print("\n--- Your Backpack ---")

        if not PLAYER_INVENTORY:
            print("It's empty")
        else:
            for item in PLAYER_INVENTORY:
                #Accesses inventory item names
                print(f"- {item["name"]}")
    
    elif verb == "go":

        if noun:
            #Noun is direction
            try_move(noun)
        else:
            print("Go where? You must specify a direction")
    
    elif verb == "take":
        if not noun:
            print("Take what?")
            return
        
        room_items = WORLD[CURRENT_ROOM_ID]["items"]
        item_to_take = None

        #Search for item in the dictionary
        for item in room_items:
            if item["name"].lower() == noun:
                item_to_take = item
                break
        if item_to_take:
            #Removes from room list
            room_items.remove(item_to_take)
            #Add to player list
            PLAYER_INVENTORY.append(item_to_take)
            print(f"You take the {item_to_take["name"]}")
        else:
            print(f"There is no {noun} here")
    
    elif verb == "drop":
        if not noun:
            print("Drop what?")
            return
        
        item_to_drop = None
        #Search the inventory
        for item in PLAYER_INVENTORY:
            if item["name"].lower() == noun:
                item_to_drop = item
                break
        
        if item_to_drop:
            #Remove from player list
            PLAYER_INVENTORY.remove(item_to_drop)
            #Add to Room List
            WORLD[CURRENT_ROOM_ID]["items"].append[item_to_drop]
            print(f"You drop the {item_to_drop["name"]}")
        else:
            print(f"You aren't carrying a {noun}.")

def save_game(world_data):
    #Writing data to a file
    with open("TextAdventure/savegame.json", "w") as file:
        file.write(json.dumps(world_data, indent=4))

def load_game():
    #Reading data from file
    with open("TextAdventure/savegame.json", "r") as file:
        loaded_data = json.loads(file.read())
    return loaded_data
    



#Starting the game
display_room_info(CURRENT_ROOM_ID)

while True:
    command = input("\nWhat do you do?> ")

    if command.lower() == "quit":
        print("Goodbye!")
        break
    elif command.lower() == "save":
        #Convert Python Dictionary to a JSON string
        save_game([WORLD, PLAYER_INVENTORY, CURRENT_ROOM_ID])
    elif command.lower() == "load":
        loaded_data = load_game()
        WORLD, PLAYER_INVENTORY, CURRENT_ROOM_ID = loaded_data[0], loaded_data[1], loaded_data[2]

    #Using the parsing function
    verb, noun = parse_command(command)

    #Using the command handler function
    if verb:
        handle_action(verb, noun)
    else:
        print("Please enter a command")