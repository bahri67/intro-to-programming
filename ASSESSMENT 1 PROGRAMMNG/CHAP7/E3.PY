# Exercise 3: T-Shirt  :ballot_box_with_check:

#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

#arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(size, message):
    """Prints a summary of the shirt's size and the message on it."""
    print(f"The shirt size is {size} and the message printed on it is: '{message}'.")


make_shirt("L", "Keep Calm and Code On")


make_shirt(size="M", message="Python is Life")
