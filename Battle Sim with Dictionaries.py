import random
user_input = ""
player = {"HP": 25,
          "Potions": 1,
          "Gold": 10,
          "LVL": 1}

monster = {"HP": 25,
           "Potions": 1,
           "Gold": 15,
           "LVL": 1}


def battle_options(player, monster):
    print(
        "1. Attack\n"
        "2. Use Potion\n"
        "3. Run Away")
    print(f"Lvl: {player["LVL"]}\nPlayer HP: {player["HP"]}")
    print(f"Lvl: {player["LVL"]}\nMonster HP: {monster["HP"]}")
    user_input = input("Select an Option: ")
    return user_input


def roll_damage():
    damage = random.randint(1, 10)
    return damage


def calculate_damage(damage, health):
    damageTaken = health - damage
    return damageTaken


def is_critical_hit(damage):
    if damage >= 10:
        print("You got a critical hit!")
        return True
    else:
        return False


def use_potion(health):
    if health >= 25:
        print("The Potion will not have any effect")
        return health
    elif health < 25:
        heal = random.randint(1, 7)
        new_health = min(heal + health, 25)
        amount_healed = new_health - health
        print(f"Recovered {amount_healed} HP!")
        return new_health


def is_alive(health):
    if health > 0:
        return True
    else:
        return False


def monster_actions(monster, player):
    if monster["HP"] <= 11 and monster["Potions"] > 0:
        print("The monster has used a potion!")
        monster["HP"] = use_potion(monster["HP"])
        monster["Potions"] -= 1
    else:
        damage = roll_damage()
        print(f"The monster hit you for {damage} damage!")
        player["HP"] = calculate_damage(damage, player["HP"])
    return monster, player


print("You've encountered a wild monster that wants to fight!\n")
while is_alive(player["HP"]):
    user_input = battle_options(player, monster)
    if user_input == "1":
        damage = roll_damage()
        print(f"You hit the monster for {damage} damage!")
        is_critical_hit(damage)
        monster["HP"] = calculate_damage(damage, monster["HP"])
        if is_alive(monster["HP"]) == False:
            print("You've defeated the monster! Good Job!\n")
            print(f"You've gained all {monster["Gold"]} Gold from the monster")
            player["Gold"] += monster["Gold"]
            monster["Gold"] = 0
            player["LVL"] += 1
            print(f"\nYou've grown to Level {player["LVL"]}")
            break
        else:
            monster, player = monster_actions(monster, player)
        if is_alive(player["HP"]) == False:
            print("You've been defeated by the monster! Your run has ended.")
            print(f"You lose all {player["Gold"]} Gold")
            player["Gold"] = 0
            break
    elif user_input == "2":
        if player["Potions"] == 0:
            print("You are out of potions!")
        elif player["HP"] >= 25:
            print("You already have full health!")
        else:
            player["HP"] = use_potion(player["HP"])
            player["Potions"] -= 1
    elif user_input == "3":
        print("You've chosen to run away in fear like a coward!")
        print(f"You lose all {player["Gold"]} Gold")
        player["Gold"] = 0
        break
