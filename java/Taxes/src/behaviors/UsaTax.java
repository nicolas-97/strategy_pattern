package behaviors;

import interfaces.ITaxBehavior;

public class UsaTax implements ITaxBehavior{
	
	public double calculateTax(double income) {
		return income * 0.15;
	}
}
