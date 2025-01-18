# Exercise 7: Seeing the World :ballot_box_with_check:
#Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.

#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.

#•	 Show that your list is still in its original order by printing it.

#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

#•	 Show that your list is still in its original order by printing it again.

#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.

#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.



places = ["Tokyo", "Paris", "London", "New York", "Manila"]

print("Original list:", places)

sorted_places = sorted(places)
print("Alphabetical order:", sorted_places)

print("List remains unchanged:", places)

reverse_sorted_places = sorted(places, reverse=True)
print("Reverse alphabetical order:", reverse_sorted_places)

print("List remains unchanged:", places)

places.reverse()
print("List after first reverse:", places)

places.reverse()
print("List after second reverse (back to original):", places)

places.sort()
print("List after sort:", places)

places.sort(reverse=True)
print("List after reverse sort:", places)
