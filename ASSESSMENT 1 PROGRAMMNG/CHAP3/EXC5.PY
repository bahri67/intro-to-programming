# Exercise 5: Change Guest List :ballot_box_with_check:

#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#omeone else to invite.

#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.


guests = ["Ahmed", "Luigi", "Zuriel"]

for guest in guests:
    print("Dear " + guest + ", you are invited to dinner!")

unable_to_attend = guests[1]  # Let's say Luigi can't make it
print(unable_to_attend + " can't make it to dinner.")

guests[1] = "Mohammed"  

for guest in guests:
    print("Dear " + guest + ", you are invited to dinner!")
