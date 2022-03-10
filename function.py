# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):  # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money


# def withdraw(balance, money):  # 출금
#     if balance >= money:
#         print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance


# def withdraw_night(balance, money):  # 저녁에 출금
#     commission = 100  # 수수료 100원
#     return commission, balance - money - commission


# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#  같은 학교 같은 학년 같은 반 수업.
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))


# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# # 인자값의 순서가 바뀌어도 출력값의 순서에는 영향을 받지 않는다.
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t".format(
#         name, age), end=" ")  # end=" "줄바꿈을 하지 않음
#     print(lang1, lang2, lang3, lang4, lang5)


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language):  # *language 가변인자 사용 (서로 다른 인자값을 받아야할 때에 사용함)
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
