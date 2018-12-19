import random
# 石头，剪刀，布游戏
player = int(input("请输入手势：石头（1），剪刀（2），布（3）："))

computer = random.randint(1, 3)

print("玩家的手势是：%d，电脑的手势是：%d" % (player, computer))

# if player == 1:
#     if computer == 2:
#         print("玩家赢")
#     elif computer == 1:
#         print("平局")
#     else:
#         print("电脑赢")
# elif player == 2:
#     if computer == 3:
#         print("玩家赢")
#     elif computer == 2:
#         print("平局")
#     else:
#         print("电脑赢")
# elif player == 3:
#     if computer == 1:
#         print("玩家赢")
#     elif computer == 3:
#         print("平局")
#     else:
#         print("电脑赢")


if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("玩家赢")
elif player == computer:
    print("平局")
else:
    print("电脑赢")
