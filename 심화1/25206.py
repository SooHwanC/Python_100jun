grade_dict = {
    "A+": 4.5,
    "A0": 4,
    "B+": 3.5,
    "B0": 3,
    "C+": 2.5,
    "C0": 2,
    "D+": 1.5,
    "D0": 1,
    "F": 0,
}
grade_total = 0
grade_grade = 0
for i in range(20):
    A = input().split()
    if A[2] == "P":
        pass
    else:
        grade_grade += float(A[1])
        grade_score = grade_dict.get(A[2])
        grade_total += float(A[1]) * float(grade_score)
print(grade_total / grade_grade)
