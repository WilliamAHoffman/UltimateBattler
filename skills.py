import main

class Skill:
    def __init__(self, name, desc, helpful, cost, sweep, modula, selfish, index):
        self.name = name
        self.desc = desc
        self.helpful = helpful
        self.cost = cost
        self.sweep = sweep
        self.modula = modula
        self.selfish = selfish
        self.index = index


#Class^

fire = main.fire
earth = main.earth
air = main.air
water = main.water
#elements

damage_modula = 0
crit_modula = 1
pierce_modula = 2
poison_modula = 3
alert_modula = 4
healing_modula = 5
speed_modula = 6
flavor_modula = 7
elements_modula = 8
recharge_modula = 9
stun_modula = 10
block_modula = 11
chance_modula = 12
total_cooldown = 13
current_cooldown = 14
burning_modula = 15

#demo = Skill(name, desc, helpful, cost, sweep, modula, selfish, index)

nothing_modular = [[flavor_modula], ["just stood in place looking like an idiot!"]]
nothing = Skill(main.nothing, "Do nothing", False, 0, False, nothing_modular, True, 0)

recharge_modular = [[recharge_modula], [10]]
recharge = Skill(main.recharge, "Tap into yourself and regain 10 mana", True, 0, False, recharge_modular, True, 1)

fortify_modular = [[block_modula], [2]]
fortify = Skill(main.fortify, "Build up a fortification to increase defence for 2 turns", True, 10, False, fortify_modular, True, 2)

punch_modular = [[damage_modula, crit_modula], [10, 5]]
punch = Skill(main.punch, "Punch an opponent", False, 0, False, punch_modular, False, 3)

mana_blast_modular = [[damage_modula], [25]]
mana_blast = Skill(main.mana_blst, "Blast an opponent with concentrated mana", False, 10, False, mana_blast_modular, False, 4)

earth_sword_modular = [[damage_modula, elements_modula], [15, earth]]
earth_sword = Skill(main.earth_sword, "Slash down dealing earth damage", False, 8, False, earth_sword_modular, False, 5)

sliced_modular = [[damage_modula, crit_modula], [8, 30]]
sliced = Skill(main.sliced, "Slice the target with an increased chance of critical hits", False, 0, False, sliced_modular, False, 6)

earthquake_modular = [[alert_modula, damage_modula, elements_modula, total_cooldown, current_cooldown], ["is becoming one with the earth!", 30, earth, 3, 0]]
earthquake = Skill(main.earthquake, "Reach deep into the ground and cause a massive earthquake", False, 15, True, earthquake_modular, False, 7)

fire_breath_modular = [[damage_modula, crit_modula, burning_modula, elements_modula], [20, 5, 2, fire]]
fire_breath = Skill(main.fire_breath, "Burn the target with fire", False, 15, False, fire_breath_modular, False, 8)
