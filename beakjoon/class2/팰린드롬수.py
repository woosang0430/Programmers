while True:
    try:
        n = list(input())
        if n[0] == '0':
            continue
        middle = len(n)//2
        second = n[middle:]

        if len(n)%2:
            first = n[:middle+1]
        else:
            first = n[:middle]
        second = [i for i in second[::-1]]

        if first == second:
            print('yes')
        else:
            print('no')
    except:
        break