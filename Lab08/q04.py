studentscore = {}
while True:
    student = input("Input (DONE = exit): ").split()
    if student[0] == "DONE":
        break
    if student[0] in studentscore:
        print("Duplicated ID")
    elif student[0].isnumeric() and len(student[0]) == 10:
        studentscore[student[0]] = student[1]
    else:
        print("Invalid input")

studentscore = dict(sorted(studentscore.items(), key=lambda x:x[1], reverse=True))

print("Output:")
for id, score in studentscore.items():
    print(f"{id} {score}")