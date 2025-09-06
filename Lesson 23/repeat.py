studentData = {
    "id1": {
        "Name": "Sara",
        "Class": "V",
        "Subjects": "math, science, english"
    },
    "id2": {
        "Name": "David",
        "Class": "V",
        "Subjects": "math, science, english"
    },
    "id3": {
        "Name": "Sara",
        "Class": "V",
        "Subjects": "math, science, english"
    },
    "id4": {
        "Name": "Sara",
        "Class": "V",
        "Subjects": "math, science, english"
    }
}

dataNoRepeats = {}
for key,value in studentData.items():
    if value not in dataNoRepeats.values():
        dataNoRepeats[key] = value

print(studentData.items())
print(studentData.values())
print(dataNoRepeats)