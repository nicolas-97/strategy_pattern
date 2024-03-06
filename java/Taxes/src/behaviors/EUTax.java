package behaviors;

import interfaces.ITaxBehavior;

public class EUTax implements ITaxBehavior{
	
	public double calculateTax(double income) {
		if (income <= 10000) {
			return income * 0.10;
		}
		return income * 0.20;
	}
}
