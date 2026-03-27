import sys


def solve():
    # Маалыматтарды тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Сандарды сап (string) түрүндө алабыз
    a = input_data[0]
    b = input_data[1]

    # Эки сандын узундугун бирдей кылуу үчүн сол жагына 0 кошуп толуктайбыз
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry = 0
    carry_count = 0

    # Оңдон солго (акырынан башына) карай цикл
    for i in range(max_len - 1, -1, -1):
        # Учурдагы цифраларды жана мурунку кадамдан калган 'carry' кошуп эсептейбиз
        digit_sum = int(a[i]) + int(b[i]) + carry

        # Эгерде сумма 2 же андан чоң болсо, кийинки разрядка 1 өтөт
        if digit_sum >= 2:
            carry = 1
            carry_count += 1
        else:
            carry = 0

    # Жалпы өтүүлөрдүн санын чыгарабыз
    print(carry_count)


if __name__ == '__main__':
    solve()