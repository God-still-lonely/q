#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�κ־Զ
���ڣ�2021-11-28
"""
import random

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")

cpu = random.randint(0, 4)

player_choice = input("������Ҫ����ѡ��:ʯͷ/ʷ����/ֽ/����/����")

if player_choice in ("ʯͷ""ʷ����""ֽ""����""����"):

    print("������Ҫ����ѡ��:",player_choice)

else:
    print("Error: No Correct Name")


if player_choice in ("ʯͷ""ʷ����""ֽ""����""����"):

  def name_to_number():#����������ѡ���Ϊ����


    if player_choice == "ʯͷ":
        a = 0

    elif player_choice == "ʷ����":
        a = 1

    elif player_choice == "ֽ":
        a = 2

    elif player_choice == "����":
        a = 3

    elif player_choice == "����":
        a = 4

    return a

a=name_to_number()

def number_to_name(cpu):#���������������Ϊ����
    if cpu == 0:
        b = "ʯͷ"

    elif cpu == 1:
        b = "ʷ����"

    elif cpu == 2:
        b = "ֽ"

    elif cpu == 3:
        b = "����"

    elif cpu == 4:
        b = "����"

    return b

b=number_to_name(cpu)
print("�������ѡ��Ϊ��",b)


def rpsls(a,b):#���бȽ��ж�
    if a == 0:
        if b == 3 or b == 4:
            result = "��Ӯ�ˣ�"
        elif b == 0:
            result = "���ͼ��������һ����"
        else:
            result = "����Ӯ��"

    elif a == 1:
        if b == 0 or b == 4:
            result = "��Ӯ�ˣ�"
        elif b == 1:
            result = "���ͼ��������һ����"
        else:
            result = "����Ӯ��"
    elif a == 2:
        if b == 0 or b == 1:
            result = "��Ӯ�ˣ�"
        elif b == 2:
            result = "���ͼ��������һ����"
        else:
            result = "����Ӯ��"
    elif a == 3:
        if b == 1 or b == 2:
            result = "��Ӯ�ˣ�"
        elif b == 3:
            result = "���ͼ��������һ����"
        else:
            result = "����Ӯ��"
    elif a == 4:
        if b == 2 or b == 3:
            result = "��Ӯ�ˣ�"
        elif b == 4:
            result = "���ͼ��������һ����"
        else:
            result = "����Ӯ��"

    return result

���= rpsls(a,b)
print(���)
