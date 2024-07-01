from sty import fg


def error():
    print("Invalid input!")
    return


def number_check(lower, upper):
    choice = 1
    number = False
    while not number:
        try:
            choice = int(input())
            if choice in range(lower, upper+1):
                number = True
            else:
                print("Number must be between", lower, "and", str(upper) + "!")
        except:
            error()
    return choice


def list_display(lister):
    counter = 0
    amount = len(lister)
    while counter < amount:
        counter = counter + 1
        print("[" + str(counter) + "]", lister[counter - 1])
    return


def clear():
    looper = 10
    while looper > 0:
        print("")
        looper = looper - 1
    return


def selection(listed):
    choice = 0
    amount = len(listed)
    while choice == 0:
        try:
            list_display(listed)
            tempchoice = int(input("> "))
            if tempchoice in range(1, amount + 1):
                choice = tempchoice
                #print("Nice! You have chosen:", listed[choice - 1])
            else:
                error()
                clear()
        except:
            error()
            clear()
    choice = choice - 1
    return choice


def interact(lister):
    list_display(lister)
    selected, index = selection(lister)
    return selected, index

#BASIC FUNCTIONS ^


white = fg(255, 255, 255)
red = fg(255, 80, 80)
orange = fg(242, 184, 75)
yellow = fg(255, 255, 117)
light_green = fg(0, 255, 76)
green = fg(107, 143, 35)
light_blue = fg(82, 180, 255)
blue = fg(0, 123, 255)
dark_blue = fg(19, 85, 156)
purple = fg(162, 0, 255)
light_purple = fg(205, 117, 255)
gray = fg(130, 130, 130)
silver = fg(200, 230, 255)
brown = fg(150, 70, 0)
black = fg(255, 255, 255)
pink = fg(255, 105, 180)
cyan = fg(46, 161, 185)
mustard = fg(191, 144, 0)
aqua = fg(80, 255, 155)
blood = fg(133, 32, 12)
lavender = fg(136, 3, 252)
light_brown = fg(196, 87, 49)

health = light_blue + "Health" + white
mana = light_blue + "Mana" + white
defense = light_blue + "Defense" + white
shield = light_blue + "Shield" + white
fire = red + "Fire" + white
air = light_blue + "Air" + white
earth = light_brown + "Earth" + white
water = blue + "Water" + white
element = light_blue + "Element" + white
poison = light_green + "Poisoned" + white
stun = light_blue + "Stunned" + white
nothing = gray + "Nothing" + white
recharge = blue + "Recharge" + white
emma = pink + "Emma" + white
goblin = light_green + "Goblin" + white
defup = gray + "Defense up" + white
fortify = gray + "Fortify" + white
punch = gray + "Punch" + white
mana_blst = light_blue + "Mana Blast" + white
forest_guard = light_green + "Forest Guard" + white
earth_sword = light_brown + "Earth Sword" + white
david = light_purple + "David" + white
sliced = gray + "Slice" + white
earthquake = light_brown + "Earthquake" + white
fire_breath = red + "Fire Breath" + white
burning = red + "Burning" + white
dragon = blood + "Dragon" + white

print(white)

import battler