T = int(input())
 
for tc in range(1, T + 1):
 
    N = int(input())
 
    AB_list = []
    for i in range(1, N + 1):
 
        AB = list(map(int, input().split()))
        AB_list.append(AB)
 
    P = int(input())
 
    C_list = []
    for j in range(1, P + 1):
 
        C = int(input())
 
        C_list.append(C)
 
    result = []
    for y in range(P):      # C의 요소들을 하나씩 꺼내서 AB_list 의 각 범위에 들어있나 확인
        cnt = 0
        for x in range(N):
            if C_list[y] in range(AB_list[x][0], AB_list[x][1] + 1):
                cnt += 1
        result.append(cnt)
 
    print(f"#{tc} {' '.join(map(str, result))}")