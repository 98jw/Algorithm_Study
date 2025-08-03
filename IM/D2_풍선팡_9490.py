T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    arr = []
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    max_num = 0

    for x in range(N):
        for y in range(M):
            total = 0

            total += arr[x][y]  # 중심값
            distance = arr[x][y]    # 이동거리

            for i in range(1, distance+1):
                try:
                    if x-i >= 0:
                        total += arr[x-i][y]    # 상
                except:
                    pass

                try:
                    total += arr[x+i][y]    # 하
                except:
                    pass

                try:
                    if y-i >= 0:
                        total += arr[x][y-i]    # 좌
                except:
                    pass

                try:
                    total += arr[x][y+i]    # 우
                except:
                    pass

            if total > max_num:
                max_num = total        


    print(f'#{t} {max_num}')

