T = int(input())
 
for tc in range(1, T + 1):
 
    N = int(input())
 
    A = list(map(int, input().split()))
 
    A_list = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            A_list.append(A[i] * A[j])
 
    max_v = -1
    for i in A_list:
        str_i = str(i)
        temp_v = -1
        for j in range(len(str_i) - 1):
            if str_i[j] > str_i[j + 1]:
                break
        else:
            temp_v = i
        if temp_v > max_v:
            max_v = temp_v
 
    print(f"#{tc} {max_v}")