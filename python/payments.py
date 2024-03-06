# Definimos la interfaz para las estrategias de procesamiento de pagoss
class PaymentStrategy:
    def process_payment(self, amount):
        pass

# Implementación de la estrategia de procesamiento de pagos con tarjeta de crédito
class CreditCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount):
        # Lógica para procesar el pago con tarjeta de crédito
        print(f"Procesando pago de ${amount} con tarjeta de crédito")

# Implementación de la estrategia de procesamiento de pagos con PayPal
class PayPalPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount):
        # Lógica para procesar el pago con PayPal
        print(f"Procesando pago de ${amount} con PayPal")

# Implementación de la estrategia de procesamiento de pagos con Bitcoin
class BitcoinPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount):
        # Lógica para procesar el pago con Bitcoin
        print(f"Procesando pago de ${amount} con Bitcoin")

# Contexto que utiliza una estrategia para procesar pagos
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.process_payment(amount)

# Ejemplo de uso
if __name__ == "__main__":
    amount = 100
    credit_card_payment_processor = PaymentProcessor(CreditCardPaymentStrategy())
    paypal_payment_processor = PaymentProcessor(PayPalPaymentStrategy())
    bitcoin_payment_processor = PaymentProcessor(BitcoinPaymentStrategy())

    credit_card_payment_processor.process_payment(amount)
    paypal_payment_processor.process_payment(amount)
    bitcoin_payment_processor.process_payment(amount)
