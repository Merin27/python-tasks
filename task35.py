from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def processPayment(self, amount):
        print(f"Processing credit card payment of ₹{amount:.2f} using card number {self.card_number}.")

class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email
    def processPayment(self, amount):
        print(f"Processing PayPal payment of ₹{amount:.2f} using email {self.email}.")

def process_transaction(payment_method, amount):
    payment_method.processPayment(amount)

credit_card_payment = CreditCardPayment("1234-5678-9012-3456")
paypal_payment = PayPalPayment("user123@gmail.com")

process_transaction(credit_card_payment, 1000.00)
process_transaction(paypal_payment, 500.00)
