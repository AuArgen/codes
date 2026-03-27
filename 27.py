import sys


def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return


    N = int(input_data[0])

    cost = []
    idx = 1

    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        cost.append(row)


    dp = [float('inf')] * (1 << N)
    dp[0] = 0


    for mask in range(1 << N):

        worker_id = bin(mask).count('1')

        if worker_id >= N:
            continue


        for task_id in range(N):

            if not (mask & (1 << task_id)):

                new_mask = mask | (1 << task_id)

                new_cost = dp[mask] + cost[worker_id][task_id]

                if new_cost < dp[new_mask]:
                    dp[new_mask] = new_cost


    print(dp[(1 << N) - 1])


if __name__ == '__main__':
    solve()