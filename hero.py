import random

class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("Attack with", self.atkl)

    def getHp(self):
        print("Hp:", self.hp)

enemy1 = Enemy(30, 45)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(45, 75)
enemy2.getAtk()
enemy2.getHp()

#Single Line Comment

'''
Multi
Line
Comment
'''

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    #Reserve health 30
    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes with", dmg, "Damage pts. Current Hp:", playerhp)

    if playerhp > 30:
        continue
    
    print("You've got low health.. Teleported tot he nearest inn.")
    break

'''
