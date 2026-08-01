class Payment:
    def process_payment(self, amount):
        print("Processing payment of", amount)


class CreditCard(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "processed using Credit Card.")


class UPI(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "processed using UPI.")


class NetBanking(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "processed using Net Banking.")


payments = [CreditCard(), UPI(), NetBanking()]

for payment in payments:
    payment.process_payment(1000)