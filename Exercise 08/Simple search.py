(""""Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.""")

# format the list of names
no= ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# correct the name
search_name = "Sam"

# check whether the name is there
if search_name in no:
    print(f"{search_name} found in the list.")
else:
    print(f"{search_name} not found in the list.")
