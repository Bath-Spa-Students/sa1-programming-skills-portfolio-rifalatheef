# Start the loop to accept pizza toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip().lower()
    
    if topping == 'quit':
        print("Finished adding toppings to your pizza!")
        break
    else:
        print(f"I'll add {topping} to your pizza.")
