def evenwords(str1):
    str2=str1.split(' ')
    for p_zbor in str2:
        if(len(p_zbor)%2==0):
            print(p_zbor)