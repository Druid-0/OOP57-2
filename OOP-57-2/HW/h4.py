import random

get_random = lambda: random.randint(1, 100)

print(get_random())

from colorama import Fore, Back, Style, init


print(Fore.RED + "Это красный текст")
print(Fore.GREEN + "Это зеленый текст")
print(Fore.BLUE + "Это синий текст")




col = {
        'a': Fore.YELLOW + "Это желтый текст",
        'b': Fore.MAGENTA + "Это пурпурный текст",
        'c': Fore.CYAN + "Это голубой текст"
    }
rand_key = random.choice(list(col.keys()))
print(col[rand_key])

