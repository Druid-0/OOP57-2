class UserAccount:
    def __init__(self, username, password, initial_balance=0):
        self.username = username  
        self._balance = initial_balance 
        self.__password = password 
        self._logged_in = False  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f" баланс попущен на {amount}. новый баланс: {self._balance}")
        else:
            print("ниже нуля низя")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Снятие {amount} успешно, баланс: {self._balance}")
            else:
                print("деньга нема")
        else:
            print("эээ куда в минус")

    def login(self, password):
        if password == self.__password:
            self._logged_in = True
            print("Доступ разрешьён")
        else:
            self._logged_in = False
            print("Доступ запрещьён")

    def get_balance(self):
        if self._logged_in:
            return self._balance
        else:
            print("по братски акк создай сначала")
            return None
