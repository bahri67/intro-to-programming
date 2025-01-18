
## Exercise 2: Glossary :ballot_box_with_check:

#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

#* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

#their meanings as values.

#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

#each word-meaning pair in your output.


glossary = {
    "Variable": "A reserved memory location to store values.",
    "Function": "A block of reusable code that performs a specific task.",
    "Loop": "A sequence of instructions that repeats until a certain condition is met.",
    "Dictionary": "A data structure that stores key-value pairs.",
    "List": "A collection of ordered items that can be of different types."
}

for word, meaning in glossary.items():
    print(f"{word}:  {meaning}")
