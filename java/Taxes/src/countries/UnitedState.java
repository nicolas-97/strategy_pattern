package countries;

import abstracts.Country;
import behaviors.UsaTax;

public class UnitedState extends Country {

	public UnitedState(double income) {
		super(income);
		this.tax = new UsaTax();
	}

}
