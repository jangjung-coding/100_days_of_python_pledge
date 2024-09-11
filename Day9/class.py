student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    else:
        if score >= 81:
            student_grades[student] = "Exceeds Expectations"
        else:
            if score >= 71:
                student_grades[student] = "Acceptable"
            else:
                student_grades[student] = "Fail"


print(student_grades)

# 리스트와 딕셔너리 중첩하기
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

trabel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(trabel_log["France"][1]) # Lille

