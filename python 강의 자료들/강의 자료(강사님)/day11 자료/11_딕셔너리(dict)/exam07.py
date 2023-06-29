# 딕셔너리를 사용하여 여러 학생들의 과목별 성적을 저장하고, 
# 각 학생의 평균 성적을 계산하는 프로그램

# 학생들의 과목별 성적 딕셔너리
grades = {
    "Alice": {"math": 90, "history": 80, "chemistry": 85},
    "Bob": {"math": 78, "history": 92, "chemistry": 89},
    "Charlie": {"math": 85, "history": 85, "chemistry": 95},
    "David": {"math": 92, "history": 88, "chemistry": 75}
}

# 각 학생의 평균 성적을 저장할 딕셔너리
average_grades = {}

# 평균 성적 계산
for student, subjects in grades.items():
    total_score = 0
    subject_count = 0
    for score in subjects.values():
        total_score += score
        subject_count += 1
    average_grades[student] = total_score / subject_count

# 결과 출력
for student, average_grade in average_grades.items():
    print(f"{student}'s average grade is {average_grade:.2f}")
