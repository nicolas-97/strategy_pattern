package ducks;
import abstracts.Duck;
import behaviors.FlyWithWings;

public class MallardDuck extends Duck {

	
	public MallardDuck() {
		flyBehavior = new FlyWithWings();
	}
	
	@Override
	public void display() {
		// TODO Auto-generated method stub

	}

}
