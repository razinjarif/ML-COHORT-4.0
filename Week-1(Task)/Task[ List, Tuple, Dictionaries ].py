
""" Task 1: Lists
Write a program that:

Creates a list of 5 numbers.
Adds a new number to the list.
Removes the second number from the list.
Prints the sum of all numbers in the list."""

number=[7,8,9,10,6]
number.append(11)
print (number)
number.remove(8)
print(sum(number))

""" Task 2: Tuples
Write a program that:

Creates a tuple with the names of 5 cities.
Prints the third city in the tuple.
Converts the tuple into a list, adds a new city, and converts it back to a tuple.
Prints the modified tuple. """

cities=("dhaka","rajshahi","khulna","sylhet","Meherpur")
print(cities[2])

conlist=list(cities)
conlist.append("Cumilla")
print(conlist)
contuple=tuple(conlist)
print(contuple)

"""  Task 3: Dictionaries
Write a program that:

Creates a dictionary where keys are subject names (e.g., Math, Science) and values are the marks (e.g., 90, 85).
Adds a new subject with its mark to the dictionary.
Updates the mark for one subject.
Prints the average marks. """

marks = {
    "Math": 90,
    "Science": 85,
    "English": 88,
    "Bangla": 92,
    "ICT": 80
}

marks["Economics"] = 75
marks["Science"] = 89

total = sum(marks.values())
average = total / len(marks)
print("Updated Marks:", marks)
print("Average Marks:", average)


