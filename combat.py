from random import randrange
import time

def stats(p):
  print(p["name"], "hp:", p["health"]*"❤️")

def attack(a, b):
  print(a["name"], "attacks!")
  if a["str"] + randrange(8) > b["dex"]:
    damage = a["str"] + randrange(8)
    print(a["name"], "hits for", damage, "damage")
    b["health"] -=  damage
    stats(b)
  else:
    print(a["name"], "misses")


p1 = {
  "name": "Alex",
  "health": 30,
  "str": 5,
  "dex": 6
}

p2 = {
  "name": "Archie",
  "health": 30,
  "str": 5,
  "dex": 6
}

print("Start fight")

while p1["health"]>0 and p2["health"]>0:
  if p1["health"]>1:
    attack(p1, p2)
    print()
    time.sleep(0.5)

  if p2["health"]>1:
    attack(p2, p1)
    print()
    time.sleep(0.5)

if p1["health"]<1:
  print(p1["name"], "died. Sad.")

if p2["health"]<1:
  print(p2["name"], "died. Sad.")