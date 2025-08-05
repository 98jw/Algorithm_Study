T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    arr = []
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    
    max_num = 0
    for  x in range(N):
        for y in range(M):
            total = 0

            total += arr[x][y]    # 기준값

            try:
                if x-1 >= 0:
                    total += arr[x-1][y]    #상
            except:
                pass
            
            try:
                total += arr[x+1][y]    # 하
            except:
                pass

            try:
                if y-1 >= 0:
                    total += arr[x][y-1]    # 좌
            except:
                pass

            try:
                total += arr[x][y+1]    # 우
            except:
                pass

            if total > max_num:
                max_num = total

    print(f'#{t} {max_num}')