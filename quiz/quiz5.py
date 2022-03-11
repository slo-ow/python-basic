# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차 부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# 내 풀이 방식
# index = 1
# while index < 3:
#     with open("./report/{0}주차.txt".format(index), "w", encoding="utf8") as report:
#         report.write('''
#       - {0}주차 주간보고 -
#       부서 :
#       이름 :
#       업무 요약 :'''.format(index))
#     index += 1

# for 답안
for i in range(1, 4):
    with open("./report/" + str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
