
class BankAccount:
    def __init__(self, owner, account_number):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Имя владельца не может быть пустым")

        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Номер счёта не может быть пустым")

        self.owner = owner
        self.account_number = account_number
        self.balance = 0.0

    def _validate_amount(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError("Сумма должна быть числом")

        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

    def deposit(self, amount):
        """Пополнение счёта."""
        self._validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount):
        """Снятие денежных средств."""
        self._validate_amount(amount)

        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте")

        self.balance -= amount

    def transfer(self, recipient, amount):
        """Перевод денег на другой счёт."""
        if not isinstance(recipient, BankAccount):
            raise ValueError("Получатель должен быть банковским счётом")

        if recipient is self:
            raise ValueError("Нельзя переводить деньги на свой счёт")

        self._validate_amount(amount)

        if amount > self.balance:
            raise ValueError("Недостаточно средств для перевода")

        # Изменяем балансы только после всех проверок.
        self.balance -= amount
        recipient.balance += amount

    def get_balance(self):
        """Возвращает текущий баланс."""
        return self.balance

    def is_empty(self):
        """Проверяет, пустой ли счёт."""
        return self.balance == 0
