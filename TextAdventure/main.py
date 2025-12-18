import json

#Items

item_template = {
    "name": "Template",
    "description": "Item",
    "can_be_picked_up": False
}

item_key = {
    "name": "Key",
    "description": "A small, brass key for your room",
    "can_be_picked_up": True
}

item_newspaper = {
    "name": "Newspaper",
    "description": "An old newspaper, it tells of a previous guest going missing in the basement",
    "can_be_picked_up": True
}

item_bed = {
    "name": "Bed",
    "description": "Your bed, it looks plain but usable",
    "can_be_picked_up": False
}

item_wardrobe = {
    "name": "Wardrobe",
    "description": "Your wardrobe, it contains your spare clothes",
    "can_be_picked_up": False
}

item_guestKey = {
    "name": "GuestKey",
    "description": "A key, it is labeled with the number of the room opposite yours",
    "can_be_picked_up": True
}

item_torch = {
    "name": "Torch",
    "description": "A small, battery powered torch",
    "can_be_picked_up": True
}

item_body = {
    "name": "Body",
    "description": "The body of the previous guest of the hotel. \nOoo spooky anyway that's the end of the game bye",
    "can_be_picked_up": False
}



PLAYER_INVENTORY = []


#Areas

room_template = {
    "id": "template",
    "name": "Template Room",
    "description": "Blank Room",
    "items": [
    ],
    "exits": {
    }
}

room_lobby = {
    "id": "lobby",
    "name": "The Hotel Lobby",
    "description": "A large hotel lobby, brightly lit with blank, white walls",
    "items": [
        item_key
    ],
    "exits": {
        "north": "hallway",
        "east": "stairs"
    }
}

room_hallway = {
    "id": "hallway",
    "name": "The Hallway",
    "description": "A long hallway, painted the same white as the lobby but lined with doors with various room numbers",
    "items": [
        item_newspaper
    ],
    "exits": {
        "south": "lobby",
        "east": "room",
        "west": "guest"
    }
}

room_room = {
    "id": "room",
    "name": "Your Room",
    "description": "A plain bedroom holding a simple bed and small wardrobe for your things",
    "items": [
        item_wardrobe,
        item_bed
    ],
    "requiredItems": [
        item_key
    ],
    "exits": {
        "west": "hallway"
    }
}

room_guest = {
    "id": "guest",
    "name": "Guest Room",
    "description": "A bedroom, it appears to have been torn apart by it's previous occupant",
    "items": [
        item_torch
    ],
    "requiredItems": [
        item_guestKey
    ],
    "exits": {
        "east": "hallway"
    }
}

room_stairs = {
    "id": "stairs",
    "name": "Stairs",
    "description": "A blank white staircase, it loops around to connect the lobby to the basement",
    "items": [
        item_guestKey
    ],
    "exits": {
        "west": "lobby",
        "north": "basement"
    }
}

room_basement = {
    "id": "basement",
    "name": "The Hotel Basement",
    "description": "A Dark place",
    "items": [
        item_body
    ],
    "requiredItems": [
        item_torch
    ],
    "exits": {
        "south": "stairs"
    }
}

WORLD = {
    "lobby": room_lobby,
    "hallway": room_hallway,
    "stairs": room_stairs,
    "basement": room_basement,
    "guest": room_guest,
    "room": room_room
}

CURRENT_ROOM_ID = "lobby"


#Functions

def display_room_info(room_id):
    #retrieve's current room's entire dictionary
    current_room = WORLD[room_id]

    print(f"\n--- {current_room['name'].upper()} --- \n"
          f"{current_room['description']}")
    
    #Prints the name of every item found in the current room, if there are any
    if len(WORLD[room_id]["items"]) >= 1:
        print("You see around:")
        [print(WORLD[room_id]["items"][position]["name"]) for position in range(len(WORLD[room_id]["items"]))]    

def try_move(direction):
    global CURRENT_ROOM_ID
    allowed = 0

    #Retrieves current room's exits
    current_exits = WORLD[CURRENT_ROOM_ID]["exits"]
    
    if direction in current_exits:
        try:
            #Checks if amount of items shared by the required items and the player inventory, can work with multiple requirements
            #Uses Try+Except to account for errors created by rooms with no requirements
            if len(["" for item in WORLD[current_exits[direction]]["requiredItems"] if item["name"] in [player_item["name"] for player_item in PLAYER_INVENTORY]]) == len(WORLD[current_exits[direction]]["requiredItems"]):
                allowed = 1
        except:
            allowed = 1

        if allowed == 1:   
            #Update to new location
            CURRENT_ROOM_ID = current_exits[direction]
            display_room_info(CURRENT_ROOM_ID)
        else:
            print("You do not have what you need to go that way!")
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
                print(WORLD[WORLD[CURRENT_ROOM_ID]["exits"][noun]]["description"])
            else:
                print("There is nothing to see that way!")

    elif verb == "examine":
        if not noun:
            print("Examine what?")
        else:
            #prints item description if it matches the noun and can be found within the player inventory
            [print(PLAYER_INVENTORY[position]["description"]) for position in range(len(PLAYER_INVENTORY)) if noun in PLAYER_INVENTORY[position]["name"].lower()]
            #or within the current room
            [print(WORLD[CURRENT_ROOM_ID]["items"][position]["description"]) for position in range(len(WORLD[CURRENT_ROOM_ID]["items"])) if noun in WORLD[CURRENT_ROOM_ID]["items"][position]["name"].lower()]

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
            if item_to_take["can_be_picked_up"]:
                #Removes from room list
                room_items.remove(item_to_take)
                #Add to player list
                PLAYER_INVENTORY.append(item_to_take)
                print(f"You take the {item_to_take["name"]}")
            else:
                print("You cannot pick that up!")
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
            WORLD[CURRENT_ROOM_ID]["items"].append(item_to_drop)
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
