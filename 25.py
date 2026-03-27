import sys


def solve():
    # Маалыматтарды эстутумду көп коротпой окуу үчүн sys.stdin колдонобуз
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # Сурамдардын саны
    N = int(lines[0].strip())

    # Сурамдардын канча жолу кайталанганын сактоо үчүн сөздүк (dictionary)
    freq = {}

    for i in range(1, N + 1):
        if i < len(lines):
            query = lines[i]
            # Эгер сурам бар болсо 1ди кошобуз, жок болсо 0дөн баштайбыз
            freq[query] = freq.get(query, 0) + 1

    # Сорттоо эрежеси:
    # 1. -freq[q] (Жыштыгы боюнча кемүү тартибинде)
    # 2. q (Алфавит боюнча өсүү тартибинде)
    sorted_queries = sorted(freq.keys(), key=lambda q: (-freq[q], q))

    # Эң популярдуу 10 сурамды чыгаруу (эгер 10дон аз болсо, бардыгын чыгарат)
    for i in range(min(10, len(sorted_queries))):
        print(sorted_queries[i])


if __name__ == '__main__':
    solve()