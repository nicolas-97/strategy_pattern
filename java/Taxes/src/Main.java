import abstracts.Country;
import countries.Spain;
import countries.UnitedState;

public class Main {

	public static void main(String[] args) {
		Country usa = new UnitedState(10000);
		usa.yourTax();
		
		Country spain = new Spain(8000);
		spain.yourTax();
	}

}
