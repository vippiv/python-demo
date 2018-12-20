# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。


def calc_grade():
    socer = int(input("请输入成绩："))
    if socer >= 90:
        grade = "A"
    elif socer >= 60:
        grade = "B"
    else:
        grade = "C"

    print(grade)


calc_grade()
