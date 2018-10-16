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
