s = 'University Computer Programming'
ucpc = 'UCPC'

idx = 0
cnt = 0
for i in ucpc:
    if s.find(i, idx) == -1:
        break
    else:
        idx = s.find(i, idx)
        cnt += 1
if cnt == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')