import sys


def solve():
    # Маалыматтарды тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Биринчи айлананын маалыматтары
    x1 = int(input_data[0])
    y1 = int(input_data[1])
    r1 = int(input_data[2])

    # Экинчи айлананын маалыматтары
    x2 = int(input_data[3])
    y2 = int(input_data[4])
    r2 = int(input_data[5])

    # Борборлордун ортосундагы аралыктын квадраты
    d_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

    # Радиустардын суммасынын жана айырмасынын квадраттары
    sum_r_sq = (r1 + r2) ** 2
    diff_r_sq = (r1 - r2) ** 2

    # Эки айлана кесилишүү шартын текшерүү
    if diff_r_sq <= d_sq <= sum_r_sq:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()