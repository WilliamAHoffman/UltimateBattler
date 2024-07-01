import additions
import skills
import random
import main
import entities
import copy


def healing_modula(target, heal, user):
    val = random.randint(-5, 5)
    heal = heal + val
    target.health[1] = target.health[1] + heal
    if target.health[1] > target.health[0]:
        target.health[1] = target.health[0]
    print(user.name, "healed", target.name, "for", heal)
    return


def attack_modula(base_damage, damage_modifier):
    damage = base_damage * (damage_modifier/100 + 1)
    damage = int(damage)
    return damage


def crit_modula(base_crit, crit_modifier, damage):
    crit_chance = random.randint(1, 100)
    crit_chance = crit_chance + crit_modifier + base_crit
    if crit_chance >= 100:
        damage = damage * 2
        damage = int(damage)
        print("It's a critical hit!")
    return damage


def effect_modula(target, required_modula, effect_turns, immunity):
    looper = 0
    looper2 = 0
    apply = False
    ignore = False
    while looper2 < len(immunity):
        if immunity[looper2] == required_modula:
            ignore = True
            looper = len(immunity)
        looper2 = looper2 + 1
    if not ignore:
        while looper < len(target.attack_modula[0]):
            if target.attack_modula[0][looper] == required_modula:
                target.attack_modula[1][looper] = target.attack_modula[1][looper] + effect_turns
                looper = len(target.attack_modula[0])
                apply = True
            looper = looper + 1
        if not apply:
            target.attack_modula[0].append(required_modula)
            target.attack_modula[1].append(effect_turns)
    else:
        print(target.name, "is immune to the effect below:")
    #print(target.attack_modula)
    return

#ACTION MODULA ^


def defence(base_defence, damage, peirce):
    if not peirce:
        damage = damage - base_defence
    if damage <= 0:
        damage = 1
    return damage


#ATTACKED MODULA ^


def poison_modula(poison_turns, attacker):
    poison = int(attacker.health[1]/10)
    attacker.health[1] = attacker.health[1] - poison
    print(attacker.name, "took", poison, "poison damage!")
    poison_turns = poison_turns - 1
    return poison_turns


def burning_modula(attacker):
    fire_health = int(attacker.health[0]/10)
    fire_mana = int(attacker.mana[1]/10)
    print(attacker.name, "took", fire_health, "burning damage!")
    print(attacker.name, "couldn't focus and lost", fire_mana, "mana due to the flames!")
    attacker.health[1] = attacker.health[1] - fire_health
    attacker.mana[1] = attacker.mana[1] - fire_mana


def elemental(target, user, move_element):
    elemental_bonus = 1
    def_element = target.element
    atk_element = move_element
    user_element = user.element
    if atk_element == user_element:
        elemental_bonus = 1.2
        print(user.name + "'s attack was enhanced by their element!")
    if atk_element == entities.fire:
        if def_element == entities.water:
            elemental_bonus = elemental_bonus - 0.5
        elif def_element == entities.air:
            elemental_bonus = elemental_bonus + 0.5
    elif atk_element == entities.air:
        if def_element == entities.earth:
            elemental_bonus = elemental_bonus - 0.5
        elif def_element == entities.water:
            elemental_bonus = elemental_bonus + 0.5
    elif atk_element == entities.earth:
        if def_element == entities.water:
            elemental_bonus = elemental_bonus - 0.5
        elif def_element == entities.fire:
            elemental_bonus = elemental_bonus + 0.5
    elif atk_element == entities.water:
        if def_element == entities.earth:
            elemental_bonus = elemental_bonus - 0.5
        elif def_element == entities.fire:
            elemental_bonus = elemental_bonus + 0.5
    if elemental_bonus >= 1.5:
        print(user.name + "'s attack was very effective!")
    elif elemental_bonus <= 0.5:
        print(user.name + "'s attack was not very effective!")
    return elemental_bonus


def recharge(mana, user):
    user.mana[1] = user.mana[1] + mana
    if user.mana[1] > user.mana[0]:
        user.mana[1] = user.mana[0]
    print(user.name, "regained", mana, "mana!")
    return

#ATTACKER MODULA ^


def turn_action(move, user, target):
    print(user.name, "used", move.name)
    chance = True
    looper = 0
    damage = 0
    peirce = False
    broken = False
    elemental_bonus = 1
    stun = 0
    immunity = [-1]
    #user modula
    while looper < len(user.attack_modula[0]):
        variable = user.attack_modula[1][looper]
        used_modula = user.attack_modula[0][looper]
        if used_modula == entities.poison_modula:
            user.attack_modula[1][looper] = poison_modula(variable, user)
            if user.attack_modula[1][looper] == 0:
                user.attack_modula[1].pop(looper)
                user.attack_modula[0].pop(looper)
        if used_modula == entities.stun_modula:
            stun = 1
            user.attack_modula[1][looper] = user.attack_modula[1][looper] - 1
            if user.attack_modula[1][looper] == 0:
                user.attack_modula[1].pop(looper)
                user.attack_modula[0].pop(looper)
        if used_modula == entities.block_modula:
            user.attack_modula[1][looper] = user.attack_modula[1][looper] - 1
            if user.attack_modula[1][looper] == 0:
                user.attack_modula[1].pop(looper)
                user.attack_modula[0].pop(looper)
        if used_modula == entities.burning_modula:
            user.attack_modula[1][looper] = user.attack_modula[1][looper] - 1
            burning_modula(user)
            if user.attack_modula[1][looper] == 0:
                user.attack_modula[1].pop(looper)
                user.attack_modula[0].pop(looper)
        looper = looper + 1

    #pre attack target
    looper = 0
    while looper < len(target.attack_modula[0]):
        variable = target.attack_modula[1][looper]
        target_modula = target.attack_modula[0][looper]
        if target_modula == entities.immunity_modula:
            immunity.append(variable)
        looper = looper + 1

    #skill modula
    looper = 0
    if stun == 0:
        if target.health[1] > 0:
            while looper < len(move.modula[0]):
                variable = move.modula[1][looper]
                used_modula = move.modula[0][looper]
                if used_modula == skills.damage_modula:
                    damage = attack_modula(variable, user.attack[1])
                elif used_modula == skills.chance_modula:
                    chance = variable
                    rand = random.randint(0, 100)
                    if rand > chance:
                        chance = False
                        print("The effect failed")
                elif used_modula == skills.crit_modula:
                    damage = crit_modula(variable, user.crit[1], damage)
                elif used_modula == skills.flavor_modula:
                    print(user.name, variable)
                elif used_modula == skills.healing_modula:
                    healing_modula(target, variable, user)
                elif used_modula == skills.pierce_modula:
                    print("The attack pierced!")
                    peirce = True
                elif used_modula == skills.poison_modula:
                    if chance:
                        effect_modula(target, entities.poison_modula, variable, immunity)
                        print(user.name, "poisoned", target.name, "for", variable, "turns")
                elif used_modula == skills.elements_modula:
                    elemental_bonus = elemental(target, user, variable)
                elif used_modula == skills.recharge_modula:
                    recharge(variable, user)
                elif used_modula == skills.stun_modula:
                    if chance:
                        effect_modula(target, entities.stun_modula, variable, immunity)
                        print(user.name, "stunned", target.name, "for", variable, "turns")
                elif used_modula == skills.block_modula:
                    if chance:
                        effect_modula(target, entities.block_modula, variable, immunity)
                        print(user.name, "blocked", target.name, "for", variable, "turns")
                elif used_modula == skills.current_cooldown:
                    move.modula[1][looper] = move.modula[1][looper - 1]
                elif used_modula == skills.burning_modula:
                    if chance:
                        effect_modula(target, entities.burning_modula, variable, immunity)
                        print(user.name, "burned", target.name, "for", variable, "turns")
                looper = looper + 1
    else:
        print(user.name, "couldn't attack!")
    #target modula
    looper = 0
    while looper < len(target.attack_modula[0]):
        target_modula = target.attack_modula[0][looper]
        if target_modula == entities.block_modula:
            if damage > 0:
                damage = int(damage/2)
                print(target.name, "blocked part of the attack")
        looper = looper + 1
    #End turns
    if damage > 0:
        damage = damage * elemental_bonus
        rand_val = random.randint(-5, 5)
        damage = damage + rand_val
        if peirce == False:
            damage = damage - target.defence[1]
        if damage <= 0:
            damage = 1
        damage = int(damage)
        if target.shield[1] > 0:
            target.shield[1] = target.shield[1] - damage
            if target.shield[1] <= 0:
                broken = True
        else:
            target.health[1] = target.health[1] - damage
        print(user.name, "did", damage, "damage to", target.name)
        if broken == True:
            print(target.name + "'s shield broke!")
    return


def battle_modulas(used, targets, moves, team1, team2):
    looper = 0
    while looper < len(moves):
        move = moves[looper]
        user = used[looper]
        target = targets[looper]
        if user.health[1] > 0:
            user.mana[1] = user.mana[1] - move.cost
            if target == entities.team1:
                inside_looper = 0
                while inside_looper < len(team1):
                    target = team1[inside_looper]
                    turn_action(move, user, target)
                    inside_looper = inside_looper + 1
            elif target == entities.team2:
                inside_looper = 0
                while inside_looper < len(team2):
                    target = team2[inside_looper]
                    turn_action(move, user, target)
                    inside_looper = inside_looper + 1
            else:
                turn_action(move, user, target)
        looper = looper + 1
    input("> ")
    return


def effect_sight(entity):
    looper = 0
    effects = "Effects: "
    if entity.attack_modula[0] != []:
        while looper < len(entity.attack_modula[0]):
            modula = entity.attack_modula[0][looper]
            if modula == entities.poison_modula:
                effects = effects + " " + main.poison + ": " + str(entity.attack_modula[1][looper])
            if modula == entities.stun_modula:
                effects = effects + " " + main.stun + ": " + str(entity.attack_modula[1][looper])
            if modula == entities.block_modula:
                effects = effects + " " + main.defup + ": " + str(entity.attack_modula[1][looper])
            if modula == entities.burning_modula:
                effects = effects + " " + main.burning + ": " + str(entity.attack_modula[1][looper])
            looper = looper + 1
    if effects == "Effects: ":
        effects = effects + "None"
    return effects


def class_display(lister, type1, selected_move, used_on):
    new_list = []
    counter = 0
    amount = len(lister)
    while counter < amount:
        new_list.append(lister[counter].name)
        if type1 == "prepare":
            new_list[counter] = str(new_list[counter]) + " Using: " + str(selected_move[counter].name + " on " + str(used_on[counter].name))
        if type1 == "Intro":
            new_list[counter] = str(new_list[counter]) + " Level: " + str(lister[counter].lvl)
        else:
            new_list[counter] = str(new_list[counter]) + "\n" + main.health + ": " + str(lister[counter].health[1]) + "/" + str(lister[counter].health[0])
            if lister[counter].shield[1] > 0:
                new_list[counter] = str(new_list[counter]) + ", " + main.shield + ": " + str(lister[counter].shield[1])
            if lister[counter].defence[1] != 0:
                new_list[counter] = str(new_list[counter]) + ", " + main.defense + ": " + str(lister[counter].defence[1])
            #new_list[counter] = str(new_list[counter]) + ", " + main.element + ": " + str(lister[counter].element)
        if type1 == "prepare":
            new_list[counter] = str(new_list[counter]) + ", " + main.mana + ": " + str(lister[counter].mana[1]) + "/" + str(lister[counter].mana[0])
        effects = effect_sight(lister[counter])
        if effects != "Effects: None":
            new_list[counter] = str(new_list[counter]) + "\n" + effects
        counter = counter + 1
    main.list_display(new_list)
    return


def selected_moves_initializer(team1, team2):
    selected_moves = []
    selected_targets = []
    used_by = []
    length = len(team1)
    counter = 0
    while counter < length:
        selected_moves.append(skills.nothing)
        selected_targets.append(team2[0])
        used_by.append(team1[counter])
        counter = counter + 1
    return selected_moves, selected_targets, used_by


def random_move_selector(team1, team2):
    selected_moves = []
    selected_target = []
    selected_move_id = []
    used_by = []
    looper = 0
    while looper < len(team2):
        move_amt = len(team2[looper].moves) - 1
        random_move = random.randint(0, move_amt)
        selected_move = team2[looper].moves[random_move]
        inside_looper = 0
        while inside_looper < len(selected_move.modula[0]):
            if selected_move.modula[0][inside_looper] == skills.current_cooldown:
                if selected_move.modula[1][inside_looper] > 0:
                    selected_move = team2[looper].moves[random_move - 1]
                    inside_looper = -1
            inside_looper = inside_looper + 1
        if selected_move.helpful:
            if selected_move.selfish:
                target = team2[looper]
            else:
                random_target = random.randint(0, len(team2)-1)
                target = team2[random_target]
        else:
            random_target = random.randint(0, len(team1)-1)
            target = team1[random_target]
            while target.health[1] <= 0:
                random_target = random.randint(0, len(team1) - 1)
                target = team1[random_target]
        selected_move_id.append(random_move)
        selected_moves.append(selected_move)
        selected_target.append(target)
        used_by.append(team2[looper])
        looper = looper + 1
    alert_modula_detector(team2, selected_move_id)
    looper = 0
    while looper < len(team2):
        if selected_moves[looper].sweep == True:
            if selected_moves[looper].helpful == True:
                selected_target[looper] = entities.team2
            else:
                selected_target[looper] = entities.team1
        looper = looper + 1
    return selected_moves, selected_target, used_by


def alert_modula_detector(team, selected_moves):
    looper = 0
    while looper < len(team):
        inside_looper = 0
        modula = team[looper].moves[selected_moves[looper]].modula[0]
        while inside_looper < len(modula):
            if modula[inside_looper] == skills.alert_modula:
                print(team[looper].name, team[looper].moves[selected_moves[looper]].modula[1][inside_looper])
                inside_looper = len(team[looper].moves[selected_moves[looper]].modula[0])
            inside_looper = inside_looper + 1
        looper = looper + 1
    return


def team_positions(team):
    looper = 0
    while looper < len(team):
        team[looper].name = "(" + str(looper + 1) + ")" + str(team[looper].name)
        looper = looper + 1
    return


def move_selector(player):
    print("What do you want to use!")
    looper = 0
    move_names = []
    choice = -1
    while looper < len(player.moves):
        move_names.append(str(player.moves[looper].name) + " - " + str(player.moves[looper].desc) + " - Cost: " + str(player.moves[looper].cost))
        inside_looper = 0
        while inside_looper < len(player.moves[looper].modula[0]):
            if player.moves[looper].modula[0][inside_looper] == skills.damage_modula:
                move_names[looper] = move_names[looper] + " - Damage: " + str(player.moves[looper].modula[1][inside_looper])
            if player.moves[looper].modula[0][inside_looper] == skills.current_cooldown:
                move_names[looper] = move_names[looper] + " - Cooldown: " + str(player.moves[looper].modula[1][inside_looper])
            inside_looper = inside_looper + 1
        looper = looper + 1
    while choice == -1:
        choice = main.selection(move_names)
        if player.mana[1] < player.moves[choice].cost:
            print("You don't have enough to do this!")
            choice = -1
        inside_looper = 0
        while inside_looper < len(player.moves[choice].modula[0]):
            if player.moves[choice].modula[0][inside_looper] == skills.current_cooldown:
                if player.moves[choice].modula[1][inside_looper] != 0:
                    print("You can't use this move now!")
                    choice = -1
            inside_looper = inside_looper + 1
    looper = 0
    return player.moves[choice]


def target_selector(team1, team2):
    print("Who do you want to use this on!")
    all_entities = team1 + team2
    class_display(all_entities, 0, 0, 0)
    choice = main.number_check(0, len(all_entities))
    return all_entities[choice-1]


def speed_gate(team2_moves, team2_targets, team2_used, team1_moves, team1_targets, team1_used):
    full_moves = team1_moves + team2_moves
    full_targets = team1_targets + team2_targets
    full_used = team1_used + team2_used
    full_speeds = []
    looper = 0
    while looper < len(full_used):
        full_speeds.append(full_used[looper].speed[1])
        inside_looper = 0
        while inside_looper < len(full_moves[looper].modula[0]):
            if full_moves[looper].modula[0][inside_looper] == skills.speed_modula:
                full_speeds[looper] = full_speeds[looper] + full_moves[looper].modula[1][inside_looper]
            inside_looper = inside_looper + 1
        looper = looper + 1
    sorted_speeds = [-9999999]
    sorted_targets = []
    sorted_used = []
    sorted_moves = []
    while len(sorted_speeds) < len(full_speeds):
        looper = 0
        index_check = 0
        while looper < len(full_speeds):
            if full_speeds[looper] >= sorted_speeds[index_check]:
                sorted_speeds.insert(index_check, full_speeds[looper])
                sorted_targets.insert(index_check, full_targets[looper])
                sorted_moves.insert(index_check, full_moves[looper])
                sorted_used.insert(index_check, full_used[looper])
                index_check = 0
                looper = looper + 1
            else:
                index_check = index_check + 1
    sorted_speeds.pop(len(sorted_speeds)-1)
    #print(sorted_speeds)
    return sorted_used, sorted_targets, sorted_moves


def enemy_life(team2):
    looper = 0
    while looper < len(team2):
        if team2[looper].health[1] <= 0:
            team2.pop(looper)
        looper = looper + 1
    if team2 == []:
        win = True
        print("You won!")
    else:
        win = False
    return win


def team_life(team1):
    looper = 0
    deaths = 0
    while looper < len(team1):
        if team1[looper].health[1] <= 0:
            deaths = deaths + 1
        looper = looper + 1
    if deaths == len(team1):
        lose = True
        print("You lost...")
    else:
        lose = False
    return lose


def all_cool_downs(team1, team2):
    players = team1 + team2
    looper = 0
    while looper < len(players):
        double_looper = 0
        if players[looper].health[1] > 0:
            while double_looper < len(players[looper].moves):
                triple_looper = 0
                while triple_looper < len(players[looper].moves[double_looper].modula[0]):
                    if players[looper].moves[double_looper].modula[0][triple_looper] == skills.current_cooldown:
                        if players[looper].moves[double_looper].modula[1][triple_looper] > 0:
                            players[looper].moves[double_looper].modula[1][triple_looper] = players[looper].moves[double_looper].modula[1][triple_looper] - 1
                            print("TRUE")
                    #print(players[looper].moves[double_looper].name)
                    triple_looper = triple_looper + 1
                double_looper = double_looper + 1
        looper = looper + 1
    return


def battle_loop(team1, team2):
    end_turn = len(team1) + 2
    turn_counter = 1
    print("You encountered:")
    class_display(team2, "Intro", False, 0)
    input("> ")
    main.clear()
    while turn_counter > 0:
        win = enemy_life(team2)
        lose = team_life(team1)
        if win == True:
            return True
        if lose == True:
            return False
        all_cool_downs(team1, team2)
        team2_moves, team2_targets, team2_used = random_move_selector(team1, team2)
        team1_moves, team1_targets, team1_used = selected_moves_initializer(team1, team2)
        choice = - 1
        while choice == -1:
            print("Turn:", turn_counter)
            class_display(team1, "prepare", team1_moves, team1_targets)
            print("[" + str(end_turn - 1) + "]", "View enemies")
            print("[" + str(end_turn) + "]", "End turn")
            choice = main.number_check(1, end_turn)
            if choice < end_turn - 1:
                if team1[choice - 1].health[1] > 0:
                    team1_moves[choice - 1] = move_selector(team1[choice - 1])
                    if not team1_moves[choice - 1].sweep:
                        if not team1_moves[choice - 1].selfish:
                            team1_targets[choice - 1] = target_selector(team1, team2)
                        else:
                            team1_targets[choice - 1] = team1[choice - 1]
                    else:
                        print("Who do you want to use this on?")
                        print("[1] Your team")
                        print("[2] Other team")
                        team_choice = main.number_check(1, 2)
                        if team_choice == 1:
                            team1_targets[choice - 1] = entities.team1
                        if team_choice == 2:
                            team1_targets[choice - 1] = entities.team2
                else:
                    print(team1[choice - 1].name, "is unconscious!")
                choice = - 1
            if choice == end_turn - 1:
                class_display(team2, 0, 0, 0)
                input(">")
                choice = - 1
        sorted_used, sorted_targets, sorted_moves = speed_gate(team2_moves, team2_targets, team2_used, team1_moves, team1_targets, team1_used)
        battle_modulas(sorted_used, sorted_targets, sorted_moves, team1, team2)
        turn_counter = turn_counter + 1


def battle_startup(team, scene):
    looper = 0
    while looper < len(team):
        current = team[looper]
        levelup = ((current.lvl - 1)/10) + 1
        current.health[0] = int(current.health[0] * levelup)
        current.health[1] = current.health[0]
        current.attack[0] = int(current.attack[0] * levelup)
        current.attack[1] = current.attack[0]
        current.shield[0] = int(current.shield[0] * levelup)
        current.shield[1] = current.shield[0]
        current.defence[0] = int(current.defence[0] * levelup)
        current.defence[1] = current.defence[0]
        looper = looper + 1
    return


enemy1 = copy.deepcopy(entities.dragon)
#enemy2 = copy.deepcopy(entities.forest_guard)

additions.common_mods(enemy1, 0)

#additions.common_elements(enemy2, 9)

additions.common_levels(enemy1, 0)
#additions.common_levels(enemy2, 0)

#battle_startup([enemy1, enemy2], 0)
battle_loop([copy.deepcopy(entities.emma), copy.deepcopy(entities.david)], [enemy1])
