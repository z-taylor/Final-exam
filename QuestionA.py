def calculateAverage(list):
    avg = 0
    list.remove(min(list))
    for i in range(len(list)):
        avg += list[i]
    finalAvg = avg/(len(list))
    return finalAvg
labGrades, assignmentGrades = [], []
for i in range(13):
    labGrades.append(int(input(f"Enter grade for lab {i+1}: ")))
for i in range(7):
    assignmentGrades.append(int(input(f"Enter grade for assignment {i+1}: ")))
midtermExam = int(input("Enter your midterm exam grade: "))
finalExam = int(input("Enter your final exam grade: "))
labAvg, assignmentAvg = calculateAverage(labGrades), calculateAverage(assignmentGrades)
print(f"Lab Average (after dropping the lowest score): {labAvg}")
print(f"Assignment Average (after dropping the lowest score): {assignmentAvg}")
midtermExam = finalExam if finalExam>midtermExam else midtermExam
labAvgWeighted, assignmentAvgWeighted, midtermWeighted, finalWeighted = labAvg * 0.1, assignmentAvg * 0.4, midtermExam * 0.2, finalExam * 0.3
print("Final grade components:")
print(f"Labs (10%): {labAvgWeighted}")
print(f"Assignments (40%): {assignmentAvgWeighted}")
print(f"Midterm exam/final exam (20%): {midtermWeighted}")
print(f"Fianl exam (30%): {finalWeighted}")
finalGrade = labAvgWeighted+assignmentAvgWeighted+midtermWeighted+finalWeighted
print(f"Final Numeric Grade: {finalGrade}")
letterGrade = ""
match(finalGrade):
    case finalGrade if finalGrade>89.5:
        letterGrade = "A"
    case finalGrade if 79.5<=finalGrade<89.5:
        letterGrade = "B"
    case finalGrade if 69.5<=finalGrade<79.5:
        letterGrade = "C"
    case finalGrade if 59.5<=finalGrade<69.5:
        letterGrade = "D"
    case finalGrade if finalGrade<59.5:
        letterGrade = "F"
print(f"Letter Grade: {letterGrade}")