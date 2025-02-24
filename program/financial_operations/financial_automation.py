import random
import datetime

class User:
    """
    Представляет пользователя с балансом.

    Attributes:
        username (str): Имя пользователя.
        balance (float): Баланс пользователя.
    """

    def __init__(self, username, balance=0):
        """
        Инициализирует объект User.

        Args:
            username (str): Имя пользователя.
            balance (float, optional): Начальный баланс пользователя. По умолчанию 0.
        """
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        """Пополнение баланса пользователя.

        Args:
            amount (float): Сумма пополнения.

        Raises:
            ValueError: Если сумма пополнения меньше или равна нулю.
        """
        if amount > 0:
            self.balance += amount
            print(f"Пополнение баланса пользователя {self.username}: {amount} у.е.")
        else:
            raise ValueError("Сумма пополнения должна быть больше нуля.")

    def withdraw(self, amount):
        """Снятие средств с баланса.

        Args:
            amount (float): Сумма снятия.

        Raises:
            ValueError: Если сумма снятия меньше или равна нулю.
            ValueError: Если недостаточно средств на балансе.
        """
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Снятие средств с баланса пользователя {self.username}: {amount} у.е.")
        elif amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля.")
        else:
            raise ValueError(f"Недостаточно средств на балансе для снятия {amount} у.е.")

    def transfer(self, amount, recipient):
        """Перевод средств между пользователями.

        Args:
            amount (float): Сумма перевода.
            recipient (User): Получатель перевода.

        Raises:
            ValueError: Если недостаточно средств на балансе для перевода.
        """
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            print(f"Перевод {amount} у.е. от {self.username} пользователю {recipient.username}")
        else:
            raise ValueError(f"Недостаточно средств на балансе {self.username} для перевода {amount} у.е.")

import datetime

class FinancialReport:
    """
    Представляет финансовый отчет для пользователя.

    Attributes:
        user (User): Пользователь, для которого создается отчет.
        transactions (list): Список транзакций пользователя.
    """

    def __init__(self, user):
        """
        Инициализирует объект FinancialReport.

        Args:
            user (User): Пользователь, для которого создается отчет.
        """
        self.user = user
        self.transactions = []

    def record_transaction(self, transaction_type, amount):
        """Записывает финансовую операцию в журнал.

        Args:
            transaction_type (str): Тип транзакции (например, 'депозит', 'снятие', 'перевод').
            amount (float): Сумма транзакции.
        """
        self.transactions.append({
            "transaction_type": transaction_type,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def generate_report(self):
        """Генерирует отчет о финансовых операциях пользователя.

        Выводит на экран список всех транзакций и текущий баланс пользователя.
        """
        print(f"\nФинансовый отчет для пользователя {self.user.username}:")
        print("------------------------------------------------")
        for transaction in self.transactions:
            print(f"{transaction['date']} | {transaction['transaction_type']} | {transaction['amount']} у.е.")
        print("------------------------------------------------")
        print(f"Итого на счету: {self.user.balance} у.е.\n")


class TaxCalculator:
    """
    Рассчитывает налог на доход.

    Attributes:
        income (float): Доход пользователя.
        tax_rate (float): Ставка налога (по умолчанию 15%).
    """

    def __init__(self, income, tax_rate=0.15):
        """
        Инициализирует объект TaxCalculator.

        Args:
            income (float): Доход пользователя.
            tax_rate (float, optional): Ставка налога. По умолчанию 0.15.
        """
        self.income = income
        self.tax_rate = tax_rate

    def calculate_tax(self):
        """Рассчитывает налог на доход.

        Returns:
            float: Сумма налога, рассчитанная на основе дохода и ставки налога.
        """
        tax_amount = self.income * self.tax_rate
        print(f"Налог на доход {self.income} у.е. составит: {tax_amount} у.е.")
        return tax_amount


import random

class AutomatedFinanceSystem:
    """
    Автоматизированная финансовая система для управления пользователем.

    Attributes:
        user (User): Пользователь, для которого выполняются операции.
        report (FinancialReport): Финансовый отчет пользователя.
        tax_calculator (TaxCalculator): Калькулятор налога на доход пользователя.
    """

    def __init__(self, user):
        """
        Инициализирует объект AutomatedFinanceSystem.

        Args:
            user (User): Пользователь, для которого будет работать система.
        """
        self.user = user
        self.report = FinancialReport(user)
        self.tax_calculator = TaxCalculator(user.balance)

    def automate_operations(self):
        """Автоматически выполняет несколько операций: пополнение, перевод, снятие.

        В процессе выполнения операций:
        - Баланс пользователя пополняется случайной суммой.
        - Снимается случайная сумма, если это возможно.
        - Может быть выполнен перевод средств другому пользователю.
        """
        # Пример автоматической операции
        self.user.deposit(random.randint(50, 500))  # Пополнение баланса
        self.user.withdraw(random.randint(20, 100))  # Снятие средств
        if random.choice([True, False]):  # Рандомно решаем, будет ли перевод
            recipient = User("RecipientUser", balance=random.randint(100, 500))
            self.user.transfer(random.randint(10, 50), recipient)
        self.report.generate_report()
        self.tax_calculator.calculate_tax()


# Пример использования
if __name__ == "__main__":
    user1 = User("User1", balance=1000)
    finance_system = AutomatedFinanceSystem(user1)
    finance_system.automate_operations()
