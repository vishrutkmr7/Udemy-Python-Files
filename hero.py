import random

class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy()
enemy1.getAtk()


# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80

# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp = playerhp - dmg

#     #Reserve health 30
#     if playerhp <= 30:
#         playerhp = 30

#     print("Enemy strikes with", dmg, "Damage pts. Current Hp:", playerhp)

#     if playerhp > 30:
#         continue
    
#     print("You've got low health.. Teleported tot he nearest inn.")
#     break