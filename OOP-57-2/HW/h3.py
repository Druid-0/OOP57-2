


class UserAccount:

    def __init__(self, username, balance, password, amount=100):
     self.username = username
     self._balance = balance
     self.__password = password
     self.amount = amount
     self._logged_in = False

     def deposit(amount):
         if amount >100:
             return self.amount + 10

     def withdraw(amount):
         if amount <=100:
             print(" Доступ разрешен")
             return self.amount - 50
         else:
             print("Доступ запрешен")


     def login(password):
         if password == self.__password:
             self._logged_in = True
             print("Доступ разрешён")
         else:
             self._logged_in = False
             print("Доступ запрещён")

     def get_balance():
         if self._logged_in:
             return self._balance
         else:
             print("Ошибка: сначала войдите в аккаунт.")
             return None

usr = UserAccount()


