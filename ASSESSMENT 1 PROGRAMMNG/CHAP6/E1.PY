
## Exercise 1: Pizza Toppings :ballot_box_with_check:

#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

#print a message saying you’ll add that topping to their pizza.

while (topping := input("Enter a topping (or 'quit' to finish): ").lower()) != 'quit':
    print(f"I'll add {topping} to your pizza.")
print("Thank you! We'll prepare your pizza with the selected toppings.")
