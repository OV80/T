def isT(a, b):
    if (a+b>m) and (a+m>b) and (b+m>a):
        return True
    s=[3, 4, 23, 5, 20, 35]
    m=max(s)
    s.sort (reverse= True)

    print(s)
    for i in range (1, len(s)-1):
        for j in range (i+1, len(s)):
            if isT(s[i], s[j]):
                p=(m+s[i]+s[j])/2
                S=(p*(p-m)*(p-s[i])*(p-s[j]))**0.5
                print(S)