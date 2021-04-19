m = int(input("Digite el valor de m: "))
n = int(input("Digite el valor de n: "))
mn = m - n

fm = 1
for i in range(1,m+1):
    fm = fm * i

fn = 1
for i in range(1,n+1):
    fn = fn * i 

fmn = 1
for i in range(1,mn+1):
    fmn = fmn * i

c = fm / (fn*fmn)
print(c)
