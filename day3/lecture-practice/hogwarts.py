# students = ["Harry", "Hermione", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# for i in students:
#     print(i)

# for i in range(len(students)):
#     print(i+1, students[i])

# students = {
#     "Harry": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
#     }

# for i in students:
#     print(i, students[i], sep = ", ")

students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronous": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronous": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronous": "JRT"},
    {"Name": "Draco", "House": "Slytherin", "Patronous": None}
]

for i in students:
    print(i["Name"], i["House"], i["Patronous"], sep=", ")