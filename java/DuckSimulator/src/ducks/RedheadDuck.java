package ducks;
import abstracts.Duck;
import behaviors.FlyWithWings;

public class RedheadDuck extends Duck {

	public RedheadDuck() {
		flyBehavior = new FlyWithWings();
	}
	
	@Override
	public void display() {
		// TODO Auto-generated method stub

	}

}
