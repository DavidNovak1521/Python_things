import sys

def print_table(price, div_yield, amount):
    print(f"\n$ {round((price * div_yield / 100) * amount, 2)}")

def main():
    print(f"Python version: {sys.version.split(' ')[0]}")

    price = float(input("\nStock price: "))
    div_yield = float(input("Div yield: "))
    amount = float(input("Stock amount: "))

    print_table(price, div_yield, amount)

if __name__ == "__main__":
    main()