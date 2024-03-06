package abstracts;

import interfaces.ITaxBehavior;

public class Country {
	public ITaxBehavior tax;
	public double income;
	
	public Country(double income) {
		this.income = income;
	}
	
	public void yourTax() {
		System.out.println("El valor de tus impuestos es de  $"+tax.calculateTax(this.income));
	}
}
