from eulerutil.number_theory import numdigits

count = 0
numbef = 3, 1
denombef = 2, 1

for i in range(1000):
    num = (2 * numbef[0]) + numbef[1]
    denom = (2* denombef[0]) + denombef[1]
    
    if numdigits(num) > numdigits(denom):
        count += 1
    
    numbef = num, numbef[0]
    denombef = denom, denombef[0]
    
