


class Heroes:
    def __init__(self, name, hp, atk):
        self.name = input(name)
        self.hp = hp
        self.atk = atk
        print(f"your stats: hp {self.hp}, atk {atk}")

    def attack_hero(self):
        print(f"hero attacks - {self.atk}")
        self.hp -= self.atk



    def damage(self):
        print(f"total hp: {self.hp}")
    # self.damage = lambda: print(f"total hp: {hp}")


class Zeroes:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack_zero(self):
        print(f"zero attacks - {self.atk}")
        self.hp -= self.atk

die = lambda : print("the hero dies")

hero1 = Heroes("geroy1: ", 100, 10)
zero1 = Zeroes("zlodey1: ", 30, 20)

if hero1.hp or zero1.hp <= 0:
    print(die)

move = 1

print(hero1.hp)
hero1.attack_zero()
hero1.damage()

