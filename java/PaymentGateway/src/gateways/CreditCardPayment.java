package gateways;

import interfaces.IPayment;

public class CreditCardPayment implements IPayment{

	@Override
	public void proccessPayment(double amount) {
		System.out.println("Procesando el pago de $"+amount+" con tarjeta de credito");
	}

}
