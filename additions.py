import random
from sty import fg
import entities


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


veteran = gray + "Veteran " + white
bulky = gray + "Bulky " + white
swift = gray + "Swift " + white
weak = gray + "Weak " + white
strong = gray + "Strong " + white
armored = gray + "Armored " + white
shielded = gray + "Shielded " + white


def common_mods(entity, value):
    if value == 0:
        value = random.randint(0, 100)
    if value in range(0, 10):
        entity.name = veteran + entity.name
        entity.crit[0] = int(entity.crit[0] * 1.5)
        entity.crit[1] = entity.crit[0]
    elif value in range(11, 20):
        entity.name = bulky + entity.name
        entity.health[0] = int(entity.health[0] * 1.5)
        entity.health[1] = entity.health[0]
    elif value in range(21, 30):
        entity.name = weak + entity.name
        entity.health[0] = int(entity.health[0] * 0.8)
        entity.health[1] = entity.health[0]
    elif value in range(31, 40):
        entity.name = strong + entity.name
        entity.attack[0] = int(entity.attack[0] * 1.5)
        entity.attack[1] = entity.attack[0]
    elif value in range(41, 50):
        entity.name = armored + entity.name
        entity.defence[0] = int(entity.defence[0] * 1.2 + 3)
        entity.defence[1] = entity.defence[0]
    elif value in range(51, 60):
        entity.name = swift + entity.name
        entity.speed[0] = int(entity.speed[0] * 1.5)
        entity.speed[1] = entity.speed[0]
    elif value in range(61, 70):
        entity.name = shielded + entity.name
        entity.shield[0] = int(entity.shield[0] * 1.2 + 20)
        entity.shield[1] = entity.shield[0]


def common_elements(entity, value):
    if value == entities.earth:
        value = 1
    elif value == entities.fire:
        value = 12
    elif value == entities.air:
        value = 22
    elif value == entities.water:
        value = 32

    if value == entities.random:
        value = random.randint(0, 100)

    if value in range(0, 10):
        entity.element = entities.earth
        entity.defence[0] = int(entity.defence[0] * 1.2 + 6)
        entity.defence[1] = entity.defence[0]
        entity.speed[0] = int(entity.speed[0] * 0.5)
        entity.speed[1] = entity.speed[0]
    elif value in range(11, 20):
        entity.element = entities.fire
        entity.attack[0] = int(entity.attack[0] * 1.5)
        entity.attack[1] = entity.attack[0]
        entity.health[0] = int(entity.health[0] * 0.8)
        entity.health[1] = entity.health[0]
    elif value in range(21, 30):
        entity.element = entities.air
        entity.speed[0] = int(entity.speed[0] * 2)
        entity.speed[1] = entity.speed[0]
        entity.defence[0] = int(entity.defence[0] * 0.7 - 3)
        entity.defence[1] = entity.defence[0]
    elif value in range(31, 40):
        entity.element = entities.water
        entity.crit[0] = int(entity.crit[0] * 1.5)
        entity.crit[1] = entity.crit[0]
        entity.attack[0] = int(entity.attack[0] * 0.7)
        entity.attack[1] = entity.attack[0]
    if entity.element != entities.none:
        entity.name = entity.element + " " + entity.name


def common_levels(entity, value):
    rand = random.randint(-2, 2)
    value = value + rand
    entity.lvl = entity.lvl + value
    if entity.lvl <= 0:
        entity.lvl = 1
