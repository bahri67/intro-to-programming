# Exercise 3: Print date and Time :ballot_box_with_check:

#Write a Python program to display the current date and time.


from datetime import datetime


now = datetime.now() 

print("corrent date:", now.date())
print("current time:", now.time())

