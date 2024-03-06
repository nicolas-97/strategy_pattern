package behaviors;
import interfaces.IFlyBehavior;

public class FlyWithWings implements IFlyBehavior {

	@Override
	public void fly() {
		System.out.println("I’m flying!!");
	}

}
