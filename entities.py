import skills
import main


class Entity:
    def __init__(self, name, attack, defence, mana, health, shield, crit, lvl, speed, items, moves, attack_modula, element, index):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.mana = mana
        self.health = health
        self.shield = shield
        self.crit = crit
        self.lvl = lvl
        self.speed = speed
        self.items = items
        self.moves = moves
        self.attack_modula = attack_modula
        self.element = element
        self.index = index

#team 1 is the player team

#team 2 is the enemy team

#INDEX ZERO IS BASE WHILE INDEX 1 IS CURRENT


none = "None"
fire = main.fire
earth = main.earth
air = main.air
water = main.water
random = "Random"

#elements

poison_modula = 0
stun_modula = 1
block_modula = 2
burning_modula = 3
immunity_modula = 4

#demo = Entity(name, attack, defence, mana, health, shield, crit, lvl, speed, items, moves, attack_modula, element, index)

team2 = Entity("the enemy team", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 0, [0, 0], [], [skills.nothing], [[], []], none, -2)

team1 = Entity("your team", [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], 0, [0, 0], [], [skills.nothing], [[], []], none, -1)

emma = Entity(main.emma, [1, 1], [0, 0], [100, 100], [100, 100], [0, 0], [10, 10], 1, [10, 10], [], [skills.nothing, skills.recharge, skills.fortify, skills.punch, skills.mana_blast], [[], []], none, 0)

goblin = Entity(main.goblin, [5, 5], [0, 0], [30, 30], [50, 50], [0, 0], [0, 0], 1, [5, 5], [], [skills.punch], [[], []], none, 1)

forest_guard = Entity(main.forest_guard, [10, 10], [3, 3], [50, 50], [75, 75], [20, 20], [0, 0], 1, [2, 2], [], [skills.earth_sword, skills.fortify], [[], []], none, 2)

david = Entity(main.david, [1, 1], [3, 3], [50, 50], [50, 50], [10, 10], [10, 10], 1, [5, 5], [], [skills.nothing, skills.sliced, skills.earth_sword], [[], []], none, 3)

dragon = Entity(main.dragon, [100, 100], [10, 10], [1000, 1000], [2000, 2000], [0, 0], [1, 1], 1, [20, 20], [], [skills.fire_breath], [[immunity_modula, immunity_modula], [burning_modula, stun_modula]], fire, 4)
