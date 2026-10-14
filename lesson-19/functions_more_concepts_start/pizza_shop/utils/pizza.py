def make_pizza(*toppings, size=None, crust=None, **customizations):
    print(f"Making a {size} pizza with {crust} crust")
    print("The toppings added are:")

    for topping in toppings:
        print(f"- {topping}")

    if customizations:
        print("Special instructions:")

        for key, value in customizations.items():
            print(f"- {key}: {value}")

if __name__ == "__main__":
    make_pizza("cheese", "sauce", size=16, crust="thin", cheese="double", sauce="light")
    make_pizza("spinach", "chicken", size=12, crust="thick")
    make_pizza("pineapple", "ham", crust="medium", size=18)

