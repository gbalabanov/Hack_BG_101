class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.events=[]
        self.events.append("Account was created !")

    def __str__(self):
        return("Bank account for {} with balance of {} {}".format(self.name, self.balance, self.currency))

    def __int__(self):
        return int(self.balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self.balance += amount
        self.events.append("Deposited " + str(amount) + self.currency)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        if self.balance >= amount:
            self.balance -= amount
            self.events.append(str(amount) + self.currency + " was withdrawed !")
            return True
        if self.balance < amount:
            return False

    def transfer_to(self, other, amount):
        if amount > self.balance or self.currency != other.currency:
            return False
        else:
            other.balance += amount
            self.balance -= amount
            return True


    def history(self):
        return str(self.events)
