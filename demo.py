import sys

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            x = int(input("Enter First Number: "))
            y = int(input("Enter Second Number: "))
            result = x / y
            print(result)
        #except ValueError as e:
         #   print("Invalid Input Please Input Integer...")
        except ZeroDivisionError as e:
            print(e)
#return x / y

def main():
    calculator = Calculator()

    total = calculator.add(5, 6)
    print("sum = ", total)

    difference = calculator.subtract(4, 8)
    print ("difference= ", difference)

    product = calculator.multiplication( 5, 8)
    print ("product =", product)

    division =calculator.divide( 50, 5)
    print ("devision =", division)

if __name__ == "__main__":
    sys.exit(main())