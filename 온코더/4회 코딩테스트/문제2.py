diet = "ABCD"
breakfast = "AB"
lunch = "C"

ret = ''
diet = list(diet)
meals = breakfast + lunch

for meal in meals:
    if meal in diet:
        diet.pop(diet.index(meal))
    else:
        ret = 'CHEATER'
        break

if ret == 'CHEATER':
    pass
elif len(diet):
    ret = ''.join(diet)

print(ret)
