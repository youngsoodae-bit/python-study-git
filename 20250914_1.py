# 학생 관리 프로그램 (튜플 사용)

# 학생 정보를 입력받는 함수
def input_student_info():
    name = input("학생 이름을 입력하세요: ")
    score = int(input(f"{name} 학생의 성적을 입력하세요: "))
    return (name, score)  # 튜플로 반환

# 메인 프로그램
print("=== 학생 성적 관리 프로그램 ===")

# 학생 수 입력받기
student_count = int(input("전체 학생 수를 입력하세요: "))

# 학생들의 정보를 튜플로 저장할 리스트
students = []

# 학생 정보 입력받기
for i in range(student_count):
    print(f"\n{i+1}번째 학생 정보 입력")
    student = input_student_info()
    students.append(student)

# 튜플로 변환 (최종 데이터를 튜플로 저장)
students = tuple(students)

# 석차 계산을 위한 정렬된 튜플 생성 (성적 기준 내림차순)
ranked_students = tuple(sorted(students, key=lambda x: x[1], reverse=True))

# 결과 출력
print("\n=== 학생 성적 순위 ===")
for rank, (name, score) in enumerate(ranked_students, 1):
    print(f"{rank}등: {name} (성적: {score}점)")

# 원본 데이터 확인 (입력 순서)
print("\n=== 입력 순서대로 학생 정보 ===")
for name, score in students:
    print(f"이름: {name}, 성적: {score}점")
