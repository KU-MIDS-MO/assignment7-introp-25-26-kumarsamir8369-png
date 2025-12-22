def make_account(initial_balance):
    if initial_balance < 0:
        raise ValueError("Negative balance")

    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Invalid deposit")
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Invalid withdrawal")
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        return balance

    return deposit, withdraw
