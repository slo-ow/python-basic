# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    # ljust() = 왼쪽 정렬 후 8개의 공백 확보, rjust() 오른쪽 정렬..
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # zfill() =  3개의 공간 확보 후 비어있는 값에 대해서 0으로 채움
    print("대기번호 : " + str(num).zfill(3))

# input으로 입력을 받게되면 항상 str값으로 받게된다.
answer = input("아무 값이나 입력하세요 : ")
answer = 10
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
