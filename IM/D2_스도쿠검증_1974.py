T = int(input())
 
for tc in range(1, T +1):
 
    arr = [list(map(int, input().split())) for _ in range(9)]
 
    result = 0
 
    result_row = 0
    cnt_row = 0
    for i in range(9):      # 가로방향 확인
        my_list = [0] * 10
        for j in range(9):
            my_list[arr[i][j]] += 1
        if all(x == 1 for x in my_list[1:]):
            cnt_row += 1
    if cnt_row == 9:
        result_row = 1
 
    result_col = 0
    cnt_col = 0
    for j in range(9):      # 세로방향 확인
        my_list = [0] * 10
        for i in range(9):
            my_list[arr[i][j]] += 1
        if all(x == 1 for x in my_list[1:]):
            cnt_col += 1
    if cnt_col == 9:
        result_col = 1
 
    result_sqr = 0
    cnt_sqr = 0
    for i in range(0, 9, 3):        # 각 3*3 칸 확인
        for j in range(0, 9, 3):
            my_list = [0] * 10
            for p in range(i, i + 3):
                for q in range(j, j + 3):
                    my_list[arr[p][q]] += 1
            if all(x == 1 for x in my_list[1:]):
                cnt_sqr += 1
    if cnt_sqr == 9:
        result_sqr = 1          
     
    if result_row == 1 and result_col == 1 and result_sqr == 1:
        result = 1
 
    print(f'#{tc} {result}')