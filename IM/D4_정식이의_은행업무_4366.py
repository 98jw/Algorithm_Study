T = int(input())

for tc in range(1, T + 1):

    bin_num = list(input().strip())
    tri_num = list(input().strip())

    result = -1     # 초기값은 나올 수 없는 숫자인 음수로 설정
    for i in range(len(bin_num)):   # 입력받은 2진수를 앞에서부터 하나씩 바꿔가며 비교
        if bin_num[i] == '1':
            new_bin_num = bin_num[:]
            new_bin_num[i] = '0'
            my_num = int(''.join(new_bin_num), 2)    # 자릿수 하나 바꾼 2진수를 할당
            for j in range(len(tri_num)):
                if tri_num[j] == '2':
                    new_tri_num = tri_num[:]
                    new_tri_num[j] = '1'
                    if int(''.join(new_tri_num), 3) == my_num:   # 3진수의 숫자 하나가 2 일때, 1로 바꿔서 비교
                        result = my_num
                        break
                    else:
                        new_tri_num[j] = '0'
                        if int(''.join(new_tri_num), 3) == my_num:   # 1로 바꿨는데 아닐 시 0으로 다시 바꿔서 비교
                            result = my_num
                            break
                elif tri_num[j] == '1':
                    new_tri_num = tri_num[:]
                    new_tri_num[j] = '2'
                    if int(''.join(new_tri_num), 3) == my_num:   # 3진수의 숫자 하나가 1 일때, 2로 바꿔서 비교
                        result = my_num
                        break
                    else:
                        new_tri_num[j] = '0'
                        if int(''.join(new_tri_num), 3) == my_num:   # 2로 바꿨는데 아닐 시 0으로 다시 바꿔서 비교
                            result = my_num
                            break
                elif tri_num[j] == '0':
                    new_tri_num = tri_num[:]
                    new_tri_num[j] = '2'
                    if int(''.join(new_tri_num), 3) == my_num:   # 3진수의 숫자 하나가 0 일때, 2로 바꿔서 비교
                        result = my_num
                        break
                    else:
                        new_tri_num[j] = '1'
                        if int(''.join(new_tri_num), 3) == my_num:   # 2로 바꿨는데 아닐 시 1로 다시 바꿔서 비교
                            result = my_num
                            break
        if bin_num[i] == '0':
            new_bin_num = bin_num[:]
            new_bin_num[i] = '1'
            my_num = int(''.join(new_bin_num), 2)    # 자릿수 하나 바꾼 2진수를 할당
            for j in range(len(new_tri_num)):
                if tri_num[j] == '2':
                    new_tri_num = tri_num[:]
                    new_tri_num[j] = '1'
                    if int(''.join(new_tri_num), 3) == my_num:   # 3진수의 숫자 하나가 2 일때, 1로 바꿔서 비교
                        result = my_num
                        break
                    else:
                        new_tri_num[j] = '0'
                        if int(''.join(new_tri_num), 3) == my_num:   # 1로 바꿨는데 아닐 시 0으로 다시 바꿔서 비교
                            result = my_num
                            break
                elif tri_num[j] == '1':
                    new_tri_num = tri_num[:]
                    new_tri_num[j] = '2'
                    if int(''.join(new_tri_num), 3) == my_num:   # 3진수의 숫자 하나가 1 일때, 2로 바꿔서 비교
                        result = my_num
                        break
                    else:
                        new_tri_num[j] = '0'
                        if int(''.join(new_tri_num), 3) == my_num:   # 2로 바꿨는데 아닐 시 0으로 다시 바꿔서 비교
                            result = my_num
                            break
                elif tri_num[j] == '0':
                    new_tri_num = tri_num[:]
                    new_tri_num[j] = '2'
                    if int(''.join(new_tri_num), 3) == my_num:   # 3진수의 숫자 하나가 0 일때, 2로 바꿔서 비교
                        result = my_num
                        break
                    else:
                        new_tri_num[j] = '1'
                        if int(''.join(new_tri_num), 3) == my_num:   # 2로 바꿨는데 아닐 시 1로 다시 바꿔서 비교
                            result = my_num
                            break
        if result != -1:
            break
    
    print(f'#{tc} {result}')
