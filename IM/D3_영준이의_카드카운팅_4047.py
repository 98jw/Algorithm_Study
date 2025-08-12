T = int(input())
 
for tc in range(1, T + 1):
 
    S = input().strip()
 
    size = 3
 
    card_list = [S[i:i + size] for i in range(0, len(S), size)]
 
    result = 'CORRECT'
    for i in range(len(card_list) - 1):
        for j in range(1, len(card_list) - i):      # 겹치는 카드 검사
            if card_list[i] == card_list[i + j]:
                result = 'ERROR'
                break
        if result == 'ERROR':
            break
 
    counting_sort_S = [0] * 13
    counting_sort_D = [0] * 13
    counting_sort_H = [0] * 13
    counting_sort_C = [0] * 13
 
    if result == 'CORRECT':
        for i in card_list:
            if i[0] == 'S':
                counting_sort_S[int(i[1:3]) - 1] += 1
            elif i[0] == 'D':
                counting_sort_D[int(i[1:3]) - 1] += 1
            elif i[0] == 'H':
                counting_sort_H[int(i[1:3]) - 1] += 1
            elif i[0] == 'C':
                counting_sort_C[int(i[1:3]) - 1] += 1
 
    cnt_S = 0
    cnt_D = 0
    cnt_H = 0
    cnt_C = 0
 
    for i in counting_sort_S:
        if i == 0:
            cnt_S += 1
 
    for i in counting_sort_D:
        if i == 0:
            cnt_D += 1
 
    for i in counting_sort_H:
        if i == 0:
            cnt_H += 1
 
    for i in counting_sort_C:
        if i == 0:
            cnt_C += 1
 
    if result == 'ERROR':
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {cnt_S} {cnt_D} {cnt_H} {cnt_C}')