import abstracts.Duck;
import ducks.MallardDuck;
import ducks.RedheadDuck;
import ducks.RubberDuck;

public class Main {

	public static void main(String[] args) {
		Duck mallard = new MallardDuck();
		mallard.performFly();
		
		Duck redHead = new RedheadDuck();
		redHead.performFly();
		
		Duck rubber = new RubberDuck();
		rubber.performFly();
	}

}
