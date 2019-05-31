from classes.game import Person, bcolors

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 100},
        {'name': 'Thunder', 'cost': 12, 'dmg': 124},
        {'name': 'Blizzard', 'cost': 10, 'dmg': 100}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

# print(player.generate_damage())
# print(player.generate_spell_damage(0))
# print(player.generate_spell_damage(1))
# print(player.generate_spell_damage(2))

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print('=========================================')
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("Damage caused:", dmg, "Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Player Damage taken:", enemy_damage, "Your HP:", player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN!! :)" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Lose :(" + bcolors.ENDC)
        running = False
