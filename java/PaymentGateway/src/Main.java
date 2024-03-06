import gateways.BitcoinPayment;
import gateways.CreditCardPayment;
import gateways.PayPalPayment;
import payment.PaymentProcessor;

public class Main {

	public static void main(String[] args) {
		double amount = 100.0;
		
		PaymentProcessor creditCard = new PaymentProcessor(new CreditCardPayment());
		PaymentProcessor paypal = new PaymentProcessor(new PayPalPayment());
		PaymentProcessor bitcoin = new PaymentProcessor(new BitcoinPayment());
		
		creditCard.processPayment(amount);
		paypal.processPayment(amount);
		bitcoin.processPayment(amount);

	}

}
