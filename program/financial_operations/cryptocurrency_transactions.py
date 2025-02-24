class CryptoTransaction:
    """
    Представляет транзакцию криптовалюты.

    Attributes:
        crypto_type (str): Тип криптовалюты (например, 'Bitcoin', 'Ethereum').
        amount (float): Сумма транзакции.
        date (str): Дата транзакции в формате 'YYYY-MM-DD'.
    """

    def __init__(self, crypto_type, amount, date):
        """
        Инициализирует объект CryptoTransaction.

        Args:
            crypto_type (str): Тип криптовалюты.
            amount (float): Сумма транзакции.
            date (str): Дата транзакции в формате 'YYYY-MM-DD'.
        """
        self.crypto_type = crypto_type
        self.amount = amount
        self.date = date

    def display_transaction(self):
        """
        Выводит информацию о транзакции в формате строки.

        Пример:
            >>> transaction = CryptoTransaction('Bitcoin', 0.5, '2023-10-01')
            >>> transaction.display_transaction()
            Crypto: Bitcoin, Amount: 0.5, Date: 2023-10-01
        """
        print(f"Crypto: {self.crypto_type}, Amount: {self.amount}, Date: {self.date}")

def calculate_tax(amount):
    """
    Вычисляет налог на сумму транзакции.

    Args:
        amount (float): Сумма, на которую будет рассчитан налог.

    Returns:
        float: Сумма налога, равная 20% от указанной суммы.

    Raises:
        ValueError: Если amount отрицательное.

    Пример:
        >>> calculate_tax(100)
        20.0
    """
    if amount < 0:
        raise ValueError("Сумма не может быть отрицательной.")
    return amount * 0.2
