T = int(input())

for t in range(1, T+1):

    N = int(input())

    arr = []
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    max_num = 0
    for x in range(N):
        for y in range(N):
            total = 0

            total += arr[x][y]  # 기준값

            for i in range(1, N):
                total += arr[x-i][y]    # 행
                total += arr[x][y-i]    # 열

            if total > max_num:
                max_num = total

    print(f'#{t} {max_num}')