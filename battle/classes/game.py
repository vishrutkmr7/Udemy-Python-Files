import random


class bcolors:
    HEADER = '\033[95n'
    OKBLUE = '\033[94n'
    OKGREEN = '\033[92n'
    WARNING = '\033[93n'
    FAIL = '\033[91n'
    ENDC = '\033[0n'
    BOLD = '\033[1n'
    UNDERLINE = '\033[4n'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic']
