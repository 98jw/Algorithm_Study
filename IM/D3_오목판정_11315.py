T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    arr = [list(map(str, input().strip())) for _ in range(N)]

    di = [0, 1, -1, 1]       # 오른쪽, 아래, 오른쪽 위 대각선, 오른쪽 아래 대각선
    dj = [1, 0, 1, 1]

    result = "NO"

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for direction in range(4):
                    cnt = 1
                    for distance in range(1, 5):
                        ni = i + di[direction] * distance
                        nj = j + dj[direction] * distance
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        result = 'YES'
                        break
            if result == 'YES':
                break
        if result == 'YES':
            break

    print(f'#{tc} {result}')
