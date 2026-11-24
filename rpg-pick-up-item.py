from os import system

def view_info(loc):
  print(loc["title"])
  if len(loc["items"]) > 0:
    print("You see:")
    for i in loc["items"]:
      print("  ", i)

  print("You can go:")
  for e in loc["exits"]:
    print("  ", e)

def view_player(items, message):
  if len(items) > 0:
    print("You are holding:")
    for i in items:
      print("  ", i)

  if len(message) > 0:
    print(message)


locations = {
  "tavern": {
    "title": "You find yourself in a dusty tavern full of hobbits",
    "exits": ["village"],
    "items": [],
    "requires": False
  },
  "village": {
    "title": "A quaint olde village",
    "exits": ["tavern", "tower"],
    "items": ["key"],
    "requires": False
  },
  "tower": {
    "title": "You stand before a wizards tower",
    "exits": ["village", "door"],
    "items": [],
    "requires": False
  },
  "door": {
    "title": "You use the key to unlock the door!\nYou enter the tower.\nYou read all the wizards books and now you know MAGIC!!",
    "exits": ["tower"],
    "items": [],
    "requires": "key"
  }
}


player_loc = "tavern"
player_items = []
player_message = ""

while True:
  loc = locations[player_loc]
  system("clear")
  view_info(loc)
  view_player(player_items, player_message)
  player_message = ""

  cmd = input("> ")
  action, item = cmd.split()

  if action=="go":
    next_location = locations[item]
    if next_location["requires"]:
      if next_location["requires"] in player_items:
        player_loc = item
      else:
        player_message = "There is an item required to complete this task!"
    else:
      player_loc = item

  if action=="take":
    player_items.append(item)
    loc["items"].remove(item)

  if action=="drop":
    player_items.remove(item)
    loc["items"].append(item)

