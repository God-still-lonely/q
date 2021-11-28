#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：魏志远
日期：2021-11-28
"""
import random

print("欢迎使用RPSLS游戏")
print("----------------")

cpu = random.randint(0, 4)

player_choice = input("请输入要出的选项:石头/史波克/纸/蜥蜴/剪刀")

if player_choice in ("石头""史波克""纸""蜥蜴""剪刀"):

    print("请输入要出的选项:",player_choice)

else:
    print("Error: No Correct Name")


if player_choice in ("石头""史波克""纸""蜥蜴""剪刀"):

  def name_to_number():#将玩家输入的选择改为数字


    if player_choice == "石头":
        a = 0

    elif player_choice == "史波克":
        a = 1

    elif player_choice == "纸":
        a = 2

    elif player_choice == "蜥蜴":
        a = 3

    elif player_choice == "剪刀":
        a = 4

    return a

a=name_to_number()

def number_to_name(cpu):#将电脑输出的数变为名字
    if cpu == 0:
        b = "石头"

    elif cpu == 1:
        b = "史波克"

    elif cpu == 2:
        b = "纸"

    elif cpu == 3:
        b = "蜥蜴"

    elif cpu == 4:
        b = "剪刀"

    return b

b=number_to_name(cpu)
print("计算机的选择为：",b)


def rpsls(a,b):#进行比较判断
    if a == 0:
        if b == 3 or b == 4:
            result = "你赢了！"
        elif b == 0:
            result = "您和计算机出的一样呢"
        else:
            result = "机器赢了"

    elif a == 1:
        if b == 0 or b == 4:
            result = "你赢了！"
        elif b == 1:
            result = "您和计算机出的一样呢"
        else:
            result = "机器赢了"
    elif a == 2:
        if b == 0 or b == 1:
            result = "你赢了！"
        elif b == 2:
            result = "您和计算机出的一样呢"
        else:
            result = "机器赢了"
    elif a == 3:
        if b == 1 or b == 2:
            result = "你赢了！"
        elif b == 3:
            result = "您和计算机出的一样呢"
        else:
            result = "机器赢了"
    elif a == 4:
        if b == 2 or b == 3:
            result = "你赢了！"
        elif b == 4:
            result = "您和计算机出的一样呢"
        else:
            result = "机器赢了"

    return result

结果= rpsls(a,b)
print(结果)
