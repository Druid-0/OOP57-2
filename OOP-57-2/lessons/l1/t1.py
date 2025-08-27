

class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        self.hp -= self.atk


chel = Character("Chel", 40, 20)
boss = Character("Boss", 100, 10)

# chel.attack()

