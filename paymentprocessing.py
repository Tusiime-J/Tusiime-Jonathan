# Main purpose: Demonstrates method overriding and MRO in a payment processing system.
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

    def get_transaction_details(self):
        return f"Transaction for {self.amount:.2f} units."

class CreditCardPayment(PaymentMethod):
    def __init__(self, amount, card_number, expiry_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self):
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            return f"Processing credit card payment of {self.amount:.2f} using card ending in {self.card_number[-4:]}. Status: SUCCESS."
        else:
            return f"Credit card payment failed: Invalid card details for {self.amount:.2f}."

class PayPalPayment(PaymentMethod):
    def __init__(self, amount, paypal_email):
        super().__init__(amount)
        self.paypal_email = paypal_email

    def process_payment(self):
        if "@" in self.paypal_email:
            return f"Redirecting to PayPal for payment of {self.amount:.2f} by {self.paypal_email}. Status: PENDING USER APPROVAL."
        else:
            return f"PayPal payment failed: Invalid PayPal email for {self.amount:.2f}."

class BankTransferPayment(PaymentMethod):
    def __init__(self, amount, bank_name, account_number):
        super().__init__(amount)
        self.bank_name = bank_name
        self.account_number = account_number

    def process_payment(self):
        return f"Initiating bank transfer of {self.amount:.2f} to {self.bank_name} account {self.account_number}. Status: AWAITING CONFIRMATION."

# Main purpose: Demonstrates method overriding and MRO in a payment processing system.
credit_card = CreditCardPayment(100.50, "1234567890123456", "12/25", "123")
paypal = PayPalPayment(50.00, "user@example.com")
bank_transfer = BankTransferPayment(200.75, "MyBank", "987654321")

payments = [credit_card, paypal, bank_transfer]

for payment in payments:
    print(payment.get_transaction_details())
    print(payment.process_payment())
    print("-" * 30)

print("\n--- MRO for CreditCardPayment ---")
print(CreditCardPayment.__mro__)