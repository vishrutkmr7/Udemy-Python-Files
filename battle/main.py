from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", 'elixir', "Fully restores HP/MP of 1 Party Member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's MP/HP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Steve Rogers ", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Tony Stark   ", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Thor Odinson ", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Thanos       ", 18200, 701, 525, 25, enemy_spells, [])
enemy2 = Person("Hella        ", 1250, 130, 560, 325, enemy_spells, [])
enemy3 = Person("HYDRA        ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy2, enemy1, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print('=========================================')

    print("\n\n")
    print("NAME                             HP                                       MP")
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("Choose Action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("Damage caused:", dmg, "to", enemies[enemy].name.replace(" ", ""))

            if enemies[enemy].get_hp() == 0:
                print("\n" + bcolors.FAIL + bcolors.BOLD + enemies[enemy].name.replace(" ", ""), 'has died' + bcolors.ENDC)
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\n Not Enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + " heals " + player.name.replace(" ", "") + " for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + player.name.replace(" ", "") + "'s", spell.name, "deals", str(magic_dmg), "points of damage to", enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print("\n" + bcolors.FAIL + bcolors.BOLD + enemies[enemy].name.replace(" ", ""), 'has died' + bcolors.ENDC)
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "No more", player.items[item_choice]["item"].name, "left" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == 'potion':
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name, 'heals for', str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == 'elixir':

                if item.name == 'MegaElixir':
                    for i in players:
                        i.hp = i.maxHp
                        i.mp = i.maxMp
                else:
                    player.hp = player.maxHp
                    player.mp = player.maxMp
                print(bcolors.OKGREEN + "\n" + item.name, "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name, "deals", str(item.prop), "points of damage to", enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print("\n" + bcolors.FAIL + bcolors.BOLD + enemies[enemy].name.replace(" ", ""), 'has died' + bcolors.ENDC)
                    del enemies[enemy]

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    # Check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "YOU WIN!! :)" + bcolors.ENDC)
        running = False
    # Check if enemy won
    elif defeated_players == 2:
        print(bcolors.FAIL + "You Lose :(" + bcolors.ENDC)
        running = False
    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", ""), "attacks", players[target].name.replace(" ", ""), "for", enemy_dmg, "points")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == 'white':
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name.replace(" ", "") + " for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == 'black':
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s", spell.name, "deals", str(magic_dmg), "points of damage to", players[target].name.replace(" ", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print("\n" + bcolors.FAIL + bcolors.BOLD + players[target].name.replace(" ", ""), 'has died' + bcolors.ENDC)
                    del players[target]
            # print("Enemy chose", spell, "damage is", magic_dmg)
