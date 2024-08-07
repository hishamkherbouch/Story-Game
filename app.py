import random

class Character:
    def __init__(self, name, hP, attack, style):
        self.name = name
        self.hP = hP
        self.attack = attack
        self.style = style

def createCharacter():
    name = input("Enter your character's name: ")
    styleType = ["1.Fire", "2.Water", "3.Earth", "4.Air"]
    hP = float(input("Enter your hP: "))
    attack = float(input("Enter your attack power: "))
    styleNum = int(input("Choose your attack style " + str(styleType)[1:-1]))
    if styleNum > 0 and styleNum < 5:
        styleNum = styleNum - 1
        style = styleType[styleNum]
    else:
        print("Please select a different style ")
        style = int(input("Choose your attack style " + str(styleType)[1:-1]))
    return name, hP, attack, style

name, hP, attack, style = createCharacter()
char_1 = Character(name, hP, attack, style)

print("Character:")
print("Name:", char_1.name)
print("hP:", char_1.hP)
print("Attack:", char_1.attack)
print("Style:", char_1.style)
