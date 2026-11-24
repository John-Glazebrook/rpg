locations = {}

locations[0] = {
  "title": "Tavern",
  "desc": "Welcome to the Tavern. The Vermilion Minotaur.",
  "exits": {
    "North": 1
  }
}

locations[1] = {
  "title": "Muddy Road",
  "desc": "You are in the village of Bracken Vale.",
  "exits": {
    "South" : 0,
    "North" : 2,
    "East" : 3
  }
}

locations[2] = {
  "title": "Shop",
  "desc": "The village shop",
  "exits": {
    "South" : 1
  }
}

locations[3] = {
  "title": "Spooky Woods",
  "desc": "You are deep in the Spooky Woods",
  "exits": {
    "East" : 4,
    "West" : 1
  }
}

locations[4] = {
  "title": "Outside Wizards Tower",
  "desc": "Before you is a Wizards Tower, the door is open!",
  "exits": {
    "West" : 3,
    "Door" : 5
  }
}

locations[5] = {
  "title": "Wizards Tower",
  "desc": "Inside the wizards tower",
  "exits": {
    "Door" : 4
  }
}


player = {
  "location": 0
}

def display_location(loc):
  print("+-----------------------------------------+")
  print(loc["title"])
  print(loc["desc"])
  print()
  print("Exits:")
  for k, v in loc["exits"].items():
    print(k, "-", locations[v]["title"])

def engine():
  while True:
    current_location = player["location"]
    loc = locations[current_location]
    display_location(loc)
    action = input("> ")

    if action == "Exit":
      break

    if action == "South" and "South" in loc["exits"]:
      print("\nYou go South")
      player["location"] = loc["exits"]["South"]

    if action == "North" and "North" in loc["exits"]:
      print("\nYou go North")
      player["location"] = loc["exits"]["North"]

    if action == "East" and "East" in loc["exits"]:
      print("\nYou go East")
      player["location"] = loc["exits"]["East"]

    if action == "West" and "West" in loc["exits"]:
      print("\nYou go West")
      player["location"] = loc["exits"]["West"]

    if action == "Door" and "Door" in loc["exits"]:
      print("\nYou go through the Door")
      player["location"] = loc["exits"]["Door"]
  


engine()