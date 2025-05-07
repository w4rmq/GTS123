student = {}
def summary(student):
    print("List:")
    if len(student) <= 0:
        print("> no score is recorded!")
    else:
        sum = 0
        for id,score in sorted(student.items(), key= lambda x:x[0]):
            print(f"{id} {score}")
            sum += score
        avg = sum / len(student)
        print(f"There are {len(student)} student(s). The average score is {avg:.2f} points.")

while True:
    x = input("Enter student ID and score: ")
    if x == "done 0":
        summary(student)
        break
    
    studentID, score = x.split()
    score = int(score)
    if not studentID.isnumeric() and len(studentID) != 4:
        print("Invalid ID format!")
    else:
        if studentID in student:
            print("This ID is already recorded!")
        else:
            if score < 0 or score > 100:
                print("Invalid score!")
            else:
                student[studentID] = score

