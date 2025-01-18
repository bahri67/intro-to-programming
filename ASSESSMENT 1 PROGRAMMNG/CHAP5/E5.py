
## Exercise 5: Pets :ballot_box_with_check:

#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

#each pet

pet1 = {"kind": "dog", "owner": "Sophia"}
pet2 = {"kind": "cat", "owner": "Liam"}
pet3 = {"kind": "hamster", "owner": "Emma"}
pet4 = {"kind": "rabbit", "owner": "Noah"}
pet5 = {"kind": "goldfish", "owner": "Ava"}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f"Kind of animal: {pet['kind'].title()}")
    print(f"Owner's name: {pet['owner']}\n")
