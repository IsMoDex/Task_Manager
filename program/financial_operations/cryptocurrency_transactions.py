class CryptoTransaction:
    def __init__(self, crypto_type, amount, date):
        self.crypto_type = crypto_type
        self.amount = amount
        self.date = date

    def display_transaction(self):
        print(f"Crypto: {self.crypto_type}, Amount: {self.amount}, Date: {self.date}")
