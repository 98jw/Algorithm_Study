T = int(input())
 
for tc in range(1, T + 1):
 
    A, B, C = map(int, input().split())
 
    cnt = 0     # 먹어치운 사탕 개수
    while not(A < B < C):
        if B >= C:
            B -= 1
            cnt += 1
            if B < 2:
                cnt = -1
                break
            elif B >= 2:
                continue
        elif A >= B:
            A -= 1
            cnt += 1
            if A < 1:
                cnt = -1
                break
            elif A >= 1:
                continue
 
    print(f'#{tc} {cnt}')