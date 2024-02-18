#case 1: a x bcde = fghi
#case 2: ab x cde = fghi

products = set()

#case 1 

for a in range(1, 10):
    for b in range(1, 10):
        if a == b:
            continue
        else:
            for c in range(1, 10):
                if a == c or b == c:
                    continue
                else:
                    for d in range(1, 10):
                        if a == d or b == d or c == d:
                            continue
                        else:
                            for e in range(1, 10):
                                if a == e or b == e or c == e or d == e:
                                    continue
                                else:
                                    for f in range(1, 10):
                                        if a == f or b == f or c == f or d == f or e == f:
                                            continue
                                        else:
                                            for g in range(1, 10):
                                                if a == g or b == g or c == g or d == g or e == g or f == g:
                                                    continue
                                                else:
                                                    for h in range(1, 10):
                                                        if a == h or b == h or c == h or d == h or e == h or f == h or g == h:
                                                            continue
                                                        else:
                                                            for i in range(1, 10):
                                                                if a == i or b == i or c == i or d == i or e == i or f == i or g == i or h == i:
                                                                    continue
                                                                else:
                                                                    if a * (b*1000+c*100+d*10+e) == f*1000+g*100+h*10+i or (a*10+b)*(c*100+d*10+e) == f*1000+g*100+h*10+i:
                                                                        products.add(f*1000+g*100+h*10+i)
                                        
print(sum(products))
                                    
