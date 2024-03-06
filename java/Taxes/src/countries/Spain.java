package countries;

import abstracts.Country;
import behaviors.EUTax;

public class Spain extends Country{
	
	public Spain(double income) {
		super(income);
		tax = new EUTax();
	}
}
