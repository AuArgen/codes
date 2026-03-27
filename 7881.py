import sys


def solve():
    # Рекурсиянын тереңдигин көбөйтүү
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    # Бардык баштапкы фигуралардын координаттары (4 жана 5 чарчылуу)
    base_shapes = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # 1x4 (I)
        [(0, 0), (0, 1), (1, 0), (1, 1)],  # 2x2 (O)
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # T
        [(0, 0), (0, 1), (0, 2), (1, 0)],  # L
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # J
        [(0, 0), (0, 1), (1, 1), (1, 2)],  # Z
        [(0, 1), (0, 2), (1, 0), (1, 1)],  # S
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)],  # 5-чарчылуу L (Г-форма)
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]  # 5-чарчылуу J (Г-форма)
    ]

    # Фигураларды 90 градуска айландыруу менен бардык мүмкүн болгон багыттарды түзүү
    orientations_set = set()
    for shape in base_shapes:
        for _ in range(4):
            shape = [(c, -r) for r, c in shape]
            min_r = min(r for r, c in shape)
            min_c = min(c for r, c in shape)
            norm = tuple(sorted((r - min_r, c - min_c) for r, c in shape))
            orientations_set.add(norm)
    orientations = list(orientations_set)

    memo = {}

    # Аянттын 4 жана 5тин комбинациясы менен түзүлөөрүн алдын ала текшерүүчү функция
    def can_form(x):
        if x < 0: return False
        if x % 4 == 0 or x % 5 == 0: return True
        for a in range(x // 4 + 1):
            if (x - 4 * a) % 5 == 0: return True
        return False

    # Бөлүнбөс кичинекей торчолорду толтуруучу алгоритм (Exact Cover / Backtrack)
    def solve_grid(R, C):
        placements_by_cell = [[] for _ in range(R * C)]
        for r in range(R):
            for c in range(C):
                for shape in orientations:
                    valid = True
                    cells = []
                    for dr, dc in shape:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C:
                            cells.append(nr * C + nc)
                        else:
                            valid = False
                            break
                    if valid:
                        placements_by_cell[cells[0]].append(cells)

        # Эң чоң фигураларды биринчи коюп текшерүү үчүн сорттоо
        for p_list in placements_by_cell:
            p_list.sort(key=len, reverse=True)

        grid = [0] * (R * C)
        solution = []
        iters = [0]

        def backtrack(first_empty):
            # Убакыттан ашып кетпөө үчүн коопсуздук чеги
            if iters[0] > 500000:
                return False
            iters[0] += 1

            while first_empty < R * C and grid[first_empty]:
                first_empty += 1

            if first_empty == R * C:
                return True

            for p in placements_by_cell[first_empty]:
                can_place = True
                for cell in p:
                    if grid[cell]:
                        can_place = False
                        break
                if can_place:
                    for cell in p:
                        grid[cell] = 1
                    solution.append(p)
                    if backtrack(first_empty + 1):
                        return True
                    solution.pop()
                    for cell in p:
                        grid[cell] = 0

            return False

        if backtrack(0):
            return solution
        return None

    # Динамикалык программалоо (Торчону майда бөлүктөргө бөлүү)
    def dp_solve(R, C):
        if (R, C) in memo:
            return memo[(R, C)]

        area = R * C
        if area < 4 or not can_form(area):
            memo[(R, C)] = None
            return None

        # 1. Горизонталдуу бөлүү
        for r1 in range(1, R // 2 + 1):
            r2 = R - r1
            sol1 = dp_solve(r1, C)
            if sol1 is not None:
                sol2 = dp_solve(r2, C)
                if sol2 is not None:
                    # Бул жерде sol1 өзгөрбөйт, анткени туурасы (C) бирдей
                    shifted_sol2 = [[cell + r1 * C for cell in p] for p in sol2]
                    memo[(R, C)] = sol1 + shifted_sol2
                    return memo[(R, C)]

        # 2. Вертикалдуу бөлүү
        for c1 in range(1, C // 2 + 1):
            c2 = C - c1
            sol1 = dp_solve(R, c1)
            if sol1 is not None:
                sol2 = dp_solve(R, c2)
                if sol2 is not None:
                    # МУРУНКУ КАТА УШУЛ ЖЕРДЕ БОЛГОН: sol1 үчүн да жаңы координаталарды эсептөө керек!
                    shifted_sol1 = [[(cell // c1) * C + (cell % c1) for cell in p] for p in sol1]
                    shifted_sol2 = [[(cell // c2) * C + (cell % c2) + c1 for cell in p] for p in sol2]

                    memo[(R, C)] = shifted_sol1 + shifted_sol2
                    return memo[(R, C)]

        # Эгерде бөлүүгө мүмкүн болбосо жана аянты кичинекей болсо, түздөн-түз чечүү
        if area <= 64:
            sol = solve_grid(R, C)
            memo[(R, C)] = sol
            return sol

        memo[(R, C)] = None
        return None

    ans = dp_solve(n, m)

    # Жыйынтыкты талапка ылайык чыгаруу
    if ans is None:
        print("NO")
    else:
        print("YES")
        if t == 2:
            output_grid = [[0] * m for _ in range(n)]
            idx = 1
            for p in ans:
                for cell in p:
                    r = cell // m
                    c = cell % m
                    output_grid[r][c] = idx
                idx += 1
            # Ар бир сапты чыгаруу
            for row in output_grid:
                print(" ".join(map(str, row)))


if __name__ == '__main__':
    solve()