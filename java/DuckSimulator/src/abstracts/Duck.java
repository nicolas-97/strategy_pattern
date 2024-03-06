package abstracts;
import interfaces.IFlyBehavior;

public abstract class Duck {
	public IFlyBehavior flyBehavior;
	
	public Duck(){}

	public abstract void display();

    public void performFly() {
        flyBehavior.fly();
    }

    public void swim() {
        System.out.println("All ducks float, even decoys!");
    }
}
