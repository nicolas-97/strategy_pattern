# Definimos la interfaz para el comportamiento de vuelo
class FlyBehavior:
    def fly(self):
        pass

# Implementación del comportamiento de vuelo para patos voladores
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("¡Estoy volando!")

# Implementación del comportamiento de vuelo para patos que no pueden volar
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("No puedo volar :(")

# Definimos la interfaz para el comportamiento de sonido
class QuackBehavior:
    def quack(self):
        pass

# Implementación del comportamiento de sonido para patos que graznan
class Quack(QuackBehavior):
    def quack(self):
        print("¡Quack! ¡Quack!")

# Implementación del comportamiento de sonido para patos que hacen un sonido silencioso
class MuteQuack(QuackBehavior):
    def quack(self):
        print("...")

# Implementación del comportamiento de sonido para patos que hacen sonido de silbido
class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak! Squeak!")

# Clase base para los patos
class Duck:
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("¡Estoy nadando!")

# Clase concreta para un pato salvaje
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

# Clase concreta para un pato de goma
class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

# Ejemplo de uso
if __name__ == "__main__":
    mallard_duck = MallardDuck()
    rubber_duck = RubberDuck()

    print("Pato Mallard:")
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    mallard_duck.swim()

    print("\nPato de Goma:")
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()
    rubber_duck.swim()
