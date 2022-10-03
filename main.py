from random import randint

exe_list = []  # 创建封装题目的列表

ans_list = []  # 创建封装答案的列表


def rand_opt_num():  # 测试通过
    """随机生成运算符的数量"""
    opt_num = randint(1, 2)
    return opt_num


def rand_number():  # 测试通过
    """随机生成100以内运算数"""
    num1 = randint(1, 100)
    return num1


def rand_opt():  # 测试通过
    """随机生成运算符"""
    rand_num = randint(1, 2)
    if rand_num == 1:  # 生成1时对应加号
        opt1 = "+"
    elif rand_num == 2:  # 同理生成2时对应减号
        opt1 = "-"
    return opt1


def exe_into_list(list1, list2, opt_num):  # list1用于存题目，list2用于存答案，测试通过
    """将随机生成的题目及答案存入列表中"""
    if opt_num == 1:  # 一个运算符时
        while True:
            num1 = rand_number()
            num2 = rand_number()
            opt1 = rand_opt()
            if opt1 == "+":
                if num1 + num2 > 100:  # 保证100以内
                    continue
                else:
                    if f"{num1}{opt1}{num2}=" not in list1:  # 如果题目不在列表内，则可以出这一题，实现去重的功能
                        list1.append(f"{num1}{opt1}{num2}=")
                        list2.append(num1 + num2)
                        break
                    else:
                        continue
            if opt1 == "-":
                if num1 - num2 < 0:  # 保证100以内
                    continue
                else:
                    if f"{num1}{opt1}{num2}=" not in list1:  # 同上
                        list1.append(f"{num1}{opt1}{num2}=")
                        list2.append(num1 - num2)
                        break
                    else:
                        continue
    elif opt_num == 2:
        while True:
            num1 = rand_number()
            num2 = rand_number()
            num3 = rand_number()
            opt1 = rand_opt()
            opt2 = rand_opt()
            if opt1 == "+":
                if num1 + num2 > 100:
                    continue
                else:
                    if opt2 == "+":
                        if num1 + num2 + num3 > 100:
                            continue
                        else:
                            if f"{num1}{opt1}{num2}{opt2}{num3}=" not in list1:
                                list1.append(f"{num1}{opt1}{num2}{opt2}{num3}=")
                                list2.append(num1 + num2 + num3)
                                break
                            else:
                                continue
                    elif opt2 == "-":
                        if num1 + num2 - num3 < 0:
                            continue
                        else:
                            if f"{num1}{opt1}{num2}{opt2}{num3}=" not in list1:
                                list1.append(f"{num1}{opt1}{num2}{opt2}{num3}=")
                                list2.append(num1 + num2 - num3)
                                break
            elif opt1 == "-":
                if num1 - num2 < 0:
                    continue
                else:
                    if opt2 == "+":
                        if num1 - num2 + num3 > 100:
                            continue
                        else:
                            if f"{num1}{opt1}{num2}{opt2}{num3}=" not in list1:
                                list1.append(f"{num1}{opt1}{num2}{opt2}{num3}=")
                                list2.append(num1 - num2 + num3)
                                break
                            else:
                                continue
                    elif opt2 == "-":
                        if num1 - num2 - num3 < 0:
                            continue
                        else:
                            if f"{num1}{opt1}{num2}{opt2}{num3}=" not in list1:
                                list1.append(f"{num1}{opt1}{num2}{opt2}{num3}=")
                                list2.append(num1 - num2 - num3)
                                break


def form_exe_file(list1):  # 测试通过
    """用于生成题目的文件"""
    filename = "Exercises.txt"
    num = 1
    with open(filename, "w") as file_object:
        for list_item in list1[0:]:
            if list_item == list1[-1]:
                file_object.write(f"{num}.  {list_item}")
                num += 1
            else:
                file_object.write(f"{num}.  {list_item}\n")
                num += 1


def form_ans_file(list2):  # 测试通过
    """用于生成题目答案的文件"""
    filename = "Answers.txt"
    num = 1
    with open(filename, "w") as file_object:
        for list_item in list2[0:]:
            if list_item == list2[-1]:
                file_object.write(f"{num}.  {list_item}")
                num += 1
            else:
                file_object.write(f"{num}.  {list_item}\n")
                num += 1


# 主程序，在这里我们认为1+2和2+1是两道题目，考查了学生对加法交换律的认知，不算重复题目
exe_num_str = input("请输入题目的数量:")
exe_num = int(exe_num_str)
while exe_num != 0:
    exe_into_list(exe_list, ans_list, rand_opt_num())
    exe_num -= 1
form_exe_file(exe_list)
form_ans_file(ans_list)
