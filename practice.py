# 방법1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강"))

# 방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))

# 방법4 (v3.6 이상~)
age = 21
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
