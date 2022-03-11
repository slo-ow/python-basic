import pickle

# with문은 close() 를 따로 사용하지 않아도 자동으로 닫힘, as profile_file이라는 변수에 저장함.
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
