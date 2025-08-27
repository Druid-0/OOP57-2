class UserAccount:
    def __init__(self, username, password, initial_balance=0):
        self.username = username  # публичное поле
        self._balance = initial_balance  # защищённое поле
        self.__password = password  # приватное поле (задаётся только в __init__)
        self._logged_in = False  # отслеживаниe логина

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Баланс пополнен на {amount}. Новый баланс: {self._balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Снятие {amount} успешно. Новый баланс: {self._balance}")
            else:
                print("Ошибка: недостаточно средств на счёте.")
        else:
            print("Сумма снятия должна быть положительной.")

    def login(self, password):
        if password == self.__password:
            self._logged_in = True
            print("Доступ разрешён")
        else:
            self._logged_in = False
            print("Доступ запрещён")

    def get_balance(self):
        if self._logged_in:
            return self._balance
        else:
            print("Ошибка: сначала войдите в аккаунт.")
            return None