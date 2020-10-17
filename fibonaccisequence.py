import time
curr_ms = lambda: int(round(time.time() * 1000))
reccheck = 0

m=100 #Modulus

number = int(input("Select a number: "))
while True:
    qr = input('Print sequence? (VERY SLOW, IMPACTS ms time). [y/n]: ')
    if qr == '' or not qr[0].lower() in ['y','n']:print('Please answer with y/n!')
    else:break
if qr[0].lower() == 'y': doprint = 1
if qr[0].lower() == 'n': doprint = 0

while True:
    if number < 20:
        dr = input('Iterate with recursive function aswell? [y/n]: ')
    else:
        dr = input('Iterate with recursive function aswell? *WARNING* Your input number is more than 20 and this function most likely WILL HANG. [y/n]: ')
    if dr == '' or not dr[0].lower() in ['y','n']:print('Please answer with y/n!')
    else:break
if dr[0].lower() == 'y': dorecursive = 1
if dr[0].lower() == 'n': dorecursive = 0

while True:
    mr = input('Use mod100 on values? (Use this if you have huge input number). [y/n]: ')
    if mr == '' or not mr[0].lower() in ['y','n']:print('Please answer with y/n!')
    else:break
if mr[0].lower() == 'y': mod100 = 1
if mr[0].lower() == 'n': mod100 = 0

if mod100 == 1:
    while True:
        rr = input('Display mod100 repeating sequence? [y/n]: ')
        if rr == '' or not rr[0].lower() in ['y','n']:print('Please answer with y/n!')
        else:break
    if rr[0].lower() == 'y': reccheck = 1
    if rr[0].lower() == 'n': reccheck = 0

def f(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return f(n-1) + f(n-2)

def fib(nr):
    f0,f1=1,1
    if nr <= 0:
        print("Please enter a positive integer")
    starttime = curr_ms()
    if dorecursive == 1:
        f0 = f(nr)
    else:
        for _ in range(nr-1):
            f0,f1=f1,f0+f1
    endtime = curr_ms()
    moded = f0 % m
    if mod100 == 1:
        print(number,"th number (mod100) =",moded)
    else:
        print(number,"th number =",f0)
    print("Time taken: ",endtime-starttime,"ms")

def fib_to(n):
    fibs = [1,1] #F0, F1
    fibs1 = [1,1]
    fibs2 = [1,1]
    start2 = curr_ms()
    for _ in range(2,n): # fibs 0,1 = n+1, fibs 1,1 n
        if mod100 == 1:
            fibs.append((fibs[-1] + fibs[-2]) % m)
            fibs1.append(((2*fibs1[-1]) + fibs1[-2]) % m)  
            fibs2.append((fibs2[-1] + (2*fibs2[-2])) % m) 
        else:
            fibs.append(fibs[-1] + fibs[-2]) #normal
            fibs1.append((2*fibs1[-1]) + fibs1[-2]) #always odd 
            fibs2.append(fibs2[-1] + (2*fibs2[-2])) #always odd
 
            #fibs1.append((2*fibs1[-1]) + (2*fibs1[-2])) #always even
            #fibs2.append((2*fibs2[-1]) + (2*fibs2[-2])) #always even
    end2 = curr_ms()
  
    if reccheck == 1:
        c=[1,1];a=[]
        while(c in a)<1%m:a+=[c];c=[c[1],sum(c)%m]
        print("Sequence repeats after number: ",len(a)or 1," with modulus ", m)

    if doprint == 1:
        print("Fibonacci Sequence:")
        print("Fn-1+Fn-2: ",fibs)
        print("2Fm-1+Fm-2: ",fibs2)
        print("Fp-1 + 2Fp-2: ",fibs1)
        print("Time taken: ",end2-start2,"ms")
    else:
        print("Fibonacci Sequence (last digits):")
        print("Fn-1+Fn-2: ",fibs[-1])
        print("2Fm-1+Fm-2: ",fibs2[-1])
        print("Fp-1 + 2Fp-2: ",fibs1[-1])
        print("Time taken: ",end2-start2,"ms")


fib_to(number)
if dorecursive == 1:
    fib(number)
