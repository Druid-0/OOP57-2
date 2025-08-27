
#camel = NameSurname
#snake = name_surname

class Hero:
    # class construction
    def __init__(self, name, lvl, hp):
        #class attributes
        self.name = name
        self.lvl = lvl
        self.hp1 = hp


    def action(self):
        print(f'{self.name}, salo')


kira = Hero("kira", 100, 150)
asbek = Hero("Asbek", 100 , 100)

s = int('1')
print(kira.hp1)
# print(kirito.action()) # так низя
kira.action()
asbek.action()