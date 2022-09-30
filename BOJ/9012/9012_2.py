'''
 메모리: 30840 KB, 시간: 80 ms
 2022.09.30
 by Alub
'''
n = int(input())

for i in range(n):
    s = input()
    count = 0

    if s.count('(') == s.count(')'):
        for a in s:
            if a == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')