# Creamos una interfaz común para todos los algoritmos de impuestos
class TaxStrategy:
    def calculate_tax(self, income):
        pass

# Implementación de la estrategia para calcular impuestos en EE. UU.
class USATaxStrategy(TaxStrategy):
    def calculate_tax(self, income):
        return income * 0.15  # Tasa de impuesto fija del 15% en Estados Unidos

# Implementación de la estrategia para calcular impuestos en la UE
class EUTaxStrategy(TaxStrategy):
    def calculate_tax(self, income):
        if income <= 10000:
            return income * 0.10  # Tasa de impuesto del 10% para ingresos menores o iguales a 10000
        else:
            return income * 0.20  # Tasa de impuesto del 20% para ingresos mayores a 10000

# Contexto que utiliza una estrategia para calcular impuestos
class TaxCalculator:
    def __init__(self, tax_strategy):
        self.tax_strategy = tax_strategy

    def calculate_tax(self, income):
        return self.tax_strategy.calculate_tax(income)

# Ejemplo de uso
if __name__ == "__main__":
    income = 20000
    usa_tax_calculator = TaxCalculator(USATaxStrategy())
    eu_tax_calculator = TaxCalculator(EUTaxStrategy())

    print("Impuesto en EE. UU.:", usa_tax_calculator.calculate_tax(income))
    print("Impuesto en la UE:", eu_tax_calculator.calculate_tax(income))
