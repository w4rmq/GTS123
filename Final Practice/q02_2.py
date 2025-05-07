student = {}
def summary(student):
    ce = 0
    che = 0
    ec = 0
    ie = 0
    me = 0
    for program in student.values():
        if program[0] == "ce":
            ce += 1
        elif program[0] == "che":
            che += 1
        elif program[0] == "ec":
            ec += 1
        elif program[0] == "ie":
            ie += 1
        else:
            me += 1
    print("----SUMMARY----")
    print(f"""ce = {ce}
che = {che}
ec = {ec}
ie = {ie}
me = {me}""")
    
    print("----LIST----")
    if len(student) <= 0:
        print("The list is empty.")
    else:
        for key, value in sorted(student.items(), key=lambda x:x[1][1], reverse=True):
            print(f"{key} {value[0]} {value[1]:.2f}")

while True:
    x = input("Input: ")
    if x == "done":
        summary(student)
        break

    name, program, gpa = x.split()
    gpa = float(gpa)

    if program in ["ce", "che", "ec", "ie", "me"] and 0 <= gpa <= 4:
        student[name] = [program, gpa]
    else:
        print("ERROR")