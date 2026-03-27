import sys


def solve():
    # Маалыматтарды тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    A = int(input_data[0])
    N = int(input_data[1])

    # Эгерде сандар бирдей болсо, кадам 1ге барабар
    if A == N:
        print(1)
        return

    R = N // A

    # Эң кичинекей кадамды табуу үчүн 2ден баштап издейбиз
    for q in range(2, R + 1):
        temp = R
        # R саны q-нун даражасы экенин текшерүү
        while temp % q == 0:
            temp //= q

        # Эгерде толук бөлүнүп бүтсө, демек q минималдуу кадам
        if temp == 1:
            print(q)
            return


if __name__ == '__main__':
    solve()