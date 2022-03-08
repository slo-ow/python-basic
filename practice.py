jumin = "990120-1234567"

print("성별 : " + jumin[7])  # 7번째에 위치한 값을 가져옴
print("연 : " + jumin[0:2])  # 0 부터 2 직전까지 (0,1) 번째 값만 가져옴
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지 가져옴
print("뒤 7자리 : " + jumin[7:14])
print("뒤 전부 : " + jumin[7:])

print("뒤 7자리(뒤에서부터) : " + jumin[-7:])
# 맨 뒤에서 7번째 부터 끝까지
print("뒤 첫번째 자리 : " + jumin[-1])
# 뒤에서 첫번째
