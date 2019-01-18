# 10 is a digit now, sorry not sorry
digitnames = {0: 0, 1: 3, 2: 3,3: 5, 4: 4,5: 4,6: 3, 7: 5, 8: 5, 9: 4, 10: 3}
teens = {11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
tensnames = {20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80:6, 90:6}
mult10names = {100: 7, 1000: 8}

def howmanyletters(n: int) -> int:
    numletters = 0
    if 100 <= n <= 1000:
        if n == 100 or n == 1000:
            return 3 + mult10names[n]
        else:
            if n % 100 == 0:
                return digitnames[n//100] + 7
            elif 19 < n % 100  <= 99:
                if n % 10 == 0:
                    numletters += tensnames[n % 100]
                else:
                    numletters += tensnames[((n % 100)//10)*10] + digitnames[n % 10]
            elif 11 <= n % 100 <= 19:
                numletters += teens[n % 100]
            else:
                numletters += digitnames[n % 100]
                
            #x 'hundred and' (7 + 3)
            numletters += digitnames[n//100] + 7 + 3
 
    if 19 < n <= 99:
        if n % 10 == 0:
            return tensnames[n]
        else:
            return tensnames[n - n % 10] + digitnames[n % 10]
    
    if 11 <= n <= 19:
        return teens[n]
    
    if n <= 10:
        return digitnames[n]

    return numletters
        
acc = 0

for i in range(1, 1001):
    k = howmanyletters(i)
    print(i, k)
    acc += k
print(acc)
    
    
        
