import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    H = int(input_data[1])

    ops = []

    # Эгерде H жетиштүү чоң болсо, классикалык экиге бөлүү оптималдуу (0 ден соолук сарптайт)
    if H >= 17 or H == N:
        rem_size = N
        targets_info = []
        next_empty = 1

        while rem_size > 1:
            move_count = rem_size // 2
            target_id = next_empty
            next_empty += 1
            targets_info.append((target_id, move_count))

            for _ in range(move_count):
                ops.append(f"1 0 {target_id}")

            rem_size -= move_count

        current_stack = 0
        current_size = 1

        for target_id, initial_size in reversed(targets_info):
            ops.append(f"{current_size} {current_stack} {target_id}")
            current_size += initial_size
            current_stack = target_id

    # H өтө кичинекей болгон (3 <= H < 17) өзгөчө учур үчүн оңдолгон логика
    else:
        # Бул учурда биз китептерди 1ден көп жылдырсак HP короп кетет.
        # Ошондуктан китептерди 4 гана бөлүккө бөлүп, 3 гана HP коротобуз.
        m = N // 2
        k = (N - m) // 2
        j = (N - m - k) // 2
        r = N - m - k - j

        # 1-фаза: m китепти 1-үймөккө 1ден салуу (0 HP, анткени 0-үймөктө китеп дайыма көп же барабар болот)
        for _ in range(m):
            ops.append("1 0 1")

        # 2-фаза: k китепти 2-үймөккө 1ден салуу (0 HP)
        for _ in range(k):
            ops.append("1 0 2")

        # 3-фаза: j китепти 3-үймөккө 1ден салуу (0 HP)
        for _ in range(j):
            ops.append("1 0 3")

        # 4-фаза: Калган r китепти 1-үймөктүн үстүнө БИР МААЛДА коюу (1 HP коротот)
        if r > 0:
            ops.append(f"{r} 0 1")

        # 5-фаза: 1-үймөктүн үстүндөгү r китепти 3-үймөккө 1ден жылдыруу (0 HP)
        for _ in range(r):
            ops.append("1 1 3")

        # 6-фаза: 3-үймөктөгү (j+r) китепти БИР МААЛДА 2-үймөккө коюу (1 HP коротот)
        if j + r > 0:
            ops.append(f"{j + r} 3 2")

        # 7-фаза: 2-үймөктөгү (k+j+r) китепти БИР МААЛДА 1-үймөккө коюу (1 HP коротот)
        if k + j + r > 0:
            ops.append(f"{k + j + r} 2 1")

    # Жыйынтыкты чыгаруу (Эстутумга күч келтирбей)
    print(len(ops))
    print('\n'.join(ops))

if __name__ == '__main__':
    solve()