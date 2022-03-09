# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                  (nav)                  (5)            (1)        (!)
# 예) 생성된 비밀번호 : nav51!

from random import *
import imp


url = "http://naver.com"
my_str = url.replace("http://", "")  # 규칙 1
# print(my_str)
my_str = my_str[:my_str.index(".")]  # 규칙 2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
print(f"{url}의 비밀번호는 {password} 입니다.")


# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

users = list(range(1, 21))  # 조건 1
shuffle(users)  # 조건 2
print(users)
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :{0}".format(winners[0]))
print("커피 당첨자 :{0}".format(winners[1:]))
# print(f"치킨 당첨자 :{winners[0]}")
# print(f"커피 당첨자 :{winners[1:]}")
print("-- 축하합니다 --")


# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 3))
