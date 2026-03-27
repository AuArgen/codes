import sys


def solve():
    # Маалыматты окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    K = int(input_data[0])

    # 1-вариант: 8 жана (K-1) даана 1
    ans1 = K

    # 2-вариант: 4, 2 жана (K-2) даана 1
    ans2 = 0
    if K >= 2:
        ans2 = K * (K - 1)

    # 3-вариант: 2, 2, 2 жана (K-3) даана 1
    ans3 = 0
    if K >= 3:
        ans3 = K * (K - 1) * (K - 2) // 6

    # Бардык варианттарды кошуу
    total = ans1 + ans2 + ans3

    # Жыйынтыкты чыгаруу
    print(total)


if __name__ == '__main__':
    solve()