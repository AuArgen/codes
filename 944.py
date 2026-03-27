import sys


def solve():
    # Маалыматты тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]

    # Чоң тамгалардын балансын сактоочу сөздүк (A-Z)
    unmatched = {chr(i): 0 for i in range(65, 91)}

    is_valid = True

    for i in range(len(s)):
        char = s[i]

        if char.isupper():
            unmatched[char] += 1
        else:
            upper_char = char.upper()
            unmatched[upper_char] -= 1

            # 2-эреже: Чоң тамгасы жок туруп кичинекей тамга жазылбашы керек
            if unmatched[upper_char] < 0:
                is_valid = False
                break

            # 3-эреже: Чоң тамганын дароо аркасынан башка кичинекей тамга келбеши керек
            if i > 0 and s[i - 1].isupper() and s[i - 1] != upper_char:
                is_valid = False
                break

    # 1-эреже: Оюндун аягында бардык чоң тамгалар жабылган (0) болушу керек
    if is_valid:
        for count in unmatched.values():
            if count != 0:
                is_valid = False
                break

    # Жыйынтыкты чыгаруу
    if is_valid:
        print(0)
    else:
        # Эгер эреже бузулган болсо, эң акыркы тамганы карайбыз
        last_char = s[-1]
        if last_char.islower():
            # Акыркы тамга кичинекей болсо, 2-окуучу утулат (1 утат)
            print(1)
        else:
            # Акыркы тамга чоң болсо, 1-окуучу утулат (2 утат)
            print(2)


if __name__ == '__main__':
    solve()