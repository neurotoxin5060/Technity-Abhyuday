situation=str(input('enter\n'))
if len(situation)>=7:
    if '0000000' in situation:
        print('YES')
    
    elif '1111111' in situation:
        print('YES')

    else:
        print('NO')
else:
    print('NO')
