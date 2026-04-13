print("密码强度检测工具")
print("输入'exit'可退出程序\n")

while True:
    password = input("请输入要检测的密码:")

    if password.lower() == "exit":
        print("感谢使用，seeyou!")
        break

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    length = len(password)

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True

    score = 0
    if length >= 8:
        score += 40
    else:
        score += max(0, length * 5)

    if has_upper:
        score += 15
    if has_lower:
        score += 15
    if has_symbol:
        score += 15
    if has_digit:
        score += 15

    if score >= 80:
        level = "强"
        suggestion = "密码强度优秀"
    elif score >= 50:
        level = "中"
        suggestion = "密码强度一般，建议增加长度或添加特殊字符"
    else:
        level = "弱"
        suggestion = "密码强度过弱，请立即修改"

    print("\n===== 检测结果 =====")
    print(f"密码长度：{length} 位")
    print(f"包含大写字母：{'是' if has_upper else '否'}")
    print(f"包含小写字母：{'是' if has_lower else '否'}")
    print(f"包含数字：{'是' if has_digit else '否'}")
    print(f"包含特殊符号：{'是' if has_symbol else '否'}")
    print(f"强度分数：{score}/100")
    print(f"强度评级：{level}")
    print(f"优化建议：{suggestion}")
    print("====================\n")