package ducks;
import abstracts.Duck;
import behaviors.FlyNoWay;

public class RubberDuck extends Duck {

	public RubberDuck() {
		flyBehavior = new FlyNoWay();
	}
	
	@Override
	public void display() {
		// TODO Auto-generated method stub

	}

}
