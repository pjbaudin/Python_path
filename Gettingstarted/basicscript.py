'''
Basic operation with Python

Pierre Baudin
2018-10-16
'''

# define list
student_names = ['James', 'Kat', 'Jess', 'Mark', 'Bort', 'Frank Grimes', 'Max Power', 'Homer']

for name in student_names:
    if name == 'Bort':
        print("Found him!\n" + name)
        break
    print("Currently testing " + name)

# Dictionary example
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

# exception handling
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I cannot add these two together!")
    print(error)
print("This code executes!")