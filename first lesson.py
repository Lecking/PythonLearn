for i in range(1, 10):
    for j in range(1, i+1):
        c=i*j
        print('{}x{}={}t'.format(j, i, c), end='')
    print()