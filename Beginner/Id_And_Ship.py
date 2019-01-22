t = int(input())

d = {"B": "BattleShip", "b": "BattleShip", "C": "Cruiser", "c": "Cruiser", "D": "Destroyer", "d": "Destroyer",
     "F": "Frigate", "f": "Frigate"}

for i in range(t):
    class_id = input()
    print(d[class_id])