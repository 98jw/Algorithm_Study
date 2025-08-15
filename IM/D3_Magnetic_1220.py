# N극 (빨강) = 1, S극 (파랑) = 2, 빈칸 = 0
from asyncio import TaskGroup

for tc in range(1, 11):

    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for j in range(100):     #빨강,파랑이 세로로 연속이든 불연속이든 상관없이 나오는 경우를 센다
        flag_N = False
        for i in range(100):
            if arr[i][j] == 1:
                flag_N = True
            elif arr[i][j] == 2:
                if flag_N:
                    cnt += 1
                    flag_N = False

    print(f'#{tc} {cnt}')
