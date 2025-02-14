import random
import datetime

class User:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        """Пополнение баланса пользователя"""
        if amount > 0:
            self.balance += amount
            print(f"Пополнение баланса пользователя {self.username}: {amount} у.е.")
        else:
            print("Сумма пополнения должна быть больше нуля.")

    def withdraw(self, amount):
        """Снятие средств с баланса"""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Снятие средств с баланса пользователя {self.username}: {amount} у.е.")
        elif amount <= 0:
            print("Сумма снятия должна быть больше нуля.")
        else:
            print(f"Недостаточно средств на балансе для снятия {amount} у.е.")

    def transfer(self, amount, recipient):
        """Перевод средств между пользователями"""
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            print(f"Перевод {amount} у.е. от {self.username} пользователю {recipient.username}")
        else:
            print(f"Недостаточно средств на балансе {self.username} для перевода {amount} у.е.")

class FinancialReport:
    def __init__(self, user):
        self.user = user
        self.transactions = []

    def record_transaction(self, transaction_type, amount):
        """Записывает финансовую операцию в журнал"""
        self.transactions.append({
            "transaction_type": transaction_type,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def generate_report(self):
        """Генерирует отчет о финансовых операциях пользователя"""
        print(f"\nФинансовый отчет для пользователя {self.user.username}:")
        print("------------------------------------------------")
        for transaction in self.transactions:
            print(f"{transaction['date']} | {transaction['transaction_type']} | {transaction['amount']} у.е.")
        print("------------------------------------------------")
        print(f"Итого на счету: {self.user.balance} у.е.\n")

class TaxCalculator:
    def __init__(self, income, tax_rate=0.15):
        self.income = income
        self.tax_rate = tax_rate

    def calculate_tax(self):
        """Рассчитывает налог на доход"""
        tax_amount = self.income * self.tax_rate
        print(f"Налог на доход {self.income} у.е. составит: {tax_amount} у.е.")
        return tax_amount

class AutomatedFinanceSystem:
    def __init__(self, user):
        self.user = user
        self.report = FinancialReport(user)
        self.tax_calculator = TaxCalculator(user.balance)

    def automate_operations(self):
        """Автоматически выполняет несколько операций: пополнение, перевод, снятие"""
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
