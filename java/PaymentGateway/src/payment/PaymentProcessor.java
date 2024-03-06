package payment;

import interfaces.IPayment;

public class PaymentProcessor {
	private IPayment payment;
	
	public PaymentProcessor(IPayment payment) {
		this.payment = payment;
	}
	
	public void processPayment(double amount) {
		this.payment.proccessPayment(amount);
	}
}
