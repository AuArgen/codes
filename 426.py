import sys


def solve():
    # Маалыматтарды тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Файлдардын саны N
    n = int(input_data[0])
    idx = 1

    current_address = 0
    out = []

    for _ in range(n):
        filename = input_data[idx]
        size = int(input_data[idx + 1])
        idx += 2

        # Учурдагы даректи жана файлдын атын сактап коёбуз
        out.append(f"{current_address} {filename}")

        # Кийинки даректи эсептөө
        current_address += size

        # Эгерде дарек 16га так бөлүнбөсө, кийинки 16га бөлүнүүчү санга чейин тегеректейбиз
        if current_address % 16 != 0:
            current_address = (current_address // 16 + 1) * 16

    # Бардык файлдардан кийинки бош даректи кошуу
    out.append(str(current_address))

    # Жыйынтыкты бир убакта тез чыгаруу
    print('\n'.join(out))


if __name__ == '__main__':
    solve()