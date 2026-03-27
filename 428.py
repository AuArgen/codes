import sys
import math


def solve():
    # Маалыматтарды тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    A = int(input_data[0])
    B = int(input_data[1])
    C = int(input_data[2])

    # Уникалдуу тамырларды сактоо үчүн set колдонобуз
    roots = set()

    # 1-кашаа: X^2 + A = 0
    if A < 0:
        roots.add(math.sqrt(-A))
        roots.add(-math.sqrt(-A))
    elif A == 0:
        roots.add(0.0)

    # 2-кашаа: X^2 + B = 0
    if B < 0:
        roots.add(math.sqrt(-B))
        roots.add(-math.sqrt(-B))
    elif B == 0:
        roots.add(0.0)

    # 3-кашаа: X + C = 0
    roots.add(float(-C))

    # Сеттин (set) узундугу - бул уникалдуу чечимдердин саны
    print(len(roots))


if __name__ == '__main__':
    solve()